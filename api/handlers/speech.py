import asyncio
import logging
import threading
from pathlib import Path

import azure.cognitiveservices.speech as speechsdk
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from settings import settings

logger = logging.getLogger(__name__)

router = APIRouter()

RECOGNITION_TIMEOUT_SECONDS = 120


class SpeechRequest(BaseModel):
    audio_path: str


class SpeechResponse(BaseModel):
    result: str


def _run_recognition(audio_path: str) -> str:
    if not settings.azure_speech_key or not settings.azure_speech_region:
        raise HTTPException(status_code=503, detail="Azure Speech is not configured.")

    path = Path(audio_path)
    if not path.is_file():
        raise HTTPException(status_code=400, detail=f"Audio file not found: {audio_path}")

    speech_config = speechsdk.SpeechConfig(
        subscription=settings.azure_speech_key,
        region=settings.azure_speech_region,
    )
    speech_config.speech_recognition_language = settings.azure_speech_language

    audio_config = speechsdk.audio.AudioConfig(filename=str(path))
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    transcript: list[str] = []
    done = threading.Event()

    def on_recognized(evt: speechsdk.SpeechRecognitionEventArgs) -> None:
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech and evt.result.text:
            transcript.append(evt.result.text)

    def on_done(_: speechsdk.SessionEventArgs) -> None:
        done.set()

    recognizer.recognized.connect(on_recognized)
    recognizer.session_stopped.connect(on_done)
    recognizer.canceled.connect(on_done)

    recognizer.start_continuous_recognition()
    try:
        if not done.wait(timeout=RECOGNITION_TIMEOUT_SECONDS):
            raise HTTPException(status_code=504, detail="Speech recognition timed out.")
    finally:
        recognizer.stop_continuous_recognition()

    return " ".join(transcript).strip()


@router.post("/speech", response_model=SpeechResponse)
async def speech(req: SpeechRequest) -> SpeechResponse:
    try:
        text = await asyncio.to_thread(_run_recognition, req.audio_path)
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Speech recognition failed")
        raise HTTPException(status_code=500, detail="Speech recognition failed.") from exc
    return SpeechResponse(result=text)
