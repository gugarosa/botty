
# Entry

ENTRY_REGEX = r"^(?i)(Hey|Hello|Hi|Hallo|Bot)"

ENTRY_OPTIONS = ["Mockup", "Speech Recognition", "Chat", "Terminate"]

ENTRY_OPTIONS_RESPONSE = "Hello {name}! Please, select an option."

# States

AWAIT_OPTIONS_REGEX = r"^(Mockup|Speech Recognition|Chat)$"

AWAIT_OPTIONS_RESPONSES = [
    "Please, type anything.",
    "Please, send a voice message.",
    "Please, type your message.",
]

AWAIT_OPTIONS_STATES = ["MOCKUP", "SPEECH", "CHAT"]

# MOCKUP

MOCKUP_ERROR = "Client could not be found. Please, try again."
MOCKUP_RESPONSE = "<b>Client:</b> {client}\n<b>E-mail:</b> {email}\n<b>Phone:</b> {phone}"

# SPEECH

SPEECH_ERROR = "Could not perform speech recognition. Please, try again."
SPEECH_WAITING = "Voice message received. Please, wait."
SPEECH_RESPONSE = "<b>Transcript:</b> {transcript}"

# CHAT

CHAT_ERROR = "Chat is unavailable right now. Please, try again."
CHAT_WAITING = "Thinking ..."

# Fallback

FALLBACK_REGEX = r"^(Terminate)$"
FALLBACK_END_RESPONSE = "Session has been terminated. If you wish, please talk again with me."
FALLBACK_RETRY_RESPONSE = "Do you need anything else?"
