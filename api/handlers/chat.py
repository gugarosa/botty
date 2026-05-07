import logging

from fastapi import APIRouter, HTTPException
from openai import AsyncAzureOpenAI
from pydantic import BaseModel, Field

from settings import settings

logger = logging.getLogger(__name__)

router = APIRouter()


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)


class ChatResponse(BaseModel):
    result: str


def _client() -> AsyncAzureOpenAI:
    if not (
        settings.azure_openai_endpoint
        and settings.azure_openai_api_key
        and settings.azure_openai_deployment
    ):
        raise HTTPException(status_code=503, detail="Azure OpenAI is not configured.")
    return AsyncAzureOpenAI(
        azure_endpoint=settings.azure_openai_endpoint,
        api_key=settings.azure_openai_api_key,
        api_version=settings.azure_openai_api_version,
    )


@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    client = _client()
    try:
        completion = await client.chat.completions.create(
            model=settings.azure_openai_deployment,
            messages=[
                {"role": "system", "content": settings.azure_openai_system_prompt},
                {"role": "user", "content": req.message},
            ],
        )
    except Exception as exc:
        logger.exception("Azure OpenAI call failed")
        raise HTTPException(status_code=502, detail="Chat backend failed.") from exc

    text = completion.choices[0].message.content or ""
    return ChatResponse(result=text.strip())
