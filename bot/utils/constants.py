# encoding: utf-8

# Entry

# Regex to initiate bot flow (entry.options)
ENTRY_REGEX = '^(?i)(Hey|Hello|Hi|Hallo|Bot)'

# List of options provided by entry.options
ENTRY_OPTIONS = ['Mockup', 'Speech Recognition', 'Terminate']

# Response provided by entry.options
ENTRY_OPTIONS_RESPONSE = 'Hello {name}! Please, select an option.'

# States

## AWAIT_OPTIONS

# Regex to capture user's chosen option (order must match ENTRY_OPTIONS)
AWAIT_OPTIONS_REGEX = '^(Mockup|Speech Recognition)$'

# Responses according to possible options (order must match ENTRY_OPTIONS)
AWAIT_OPTIONS_RESPONSES = ['Please, type anything.',
                           'Please, send a voice message.']

# States according to possible options (order must match ENTRY_OPTIONS)
AWAIT_OPTIONS_STATES = ['MOCKUP', 'GOOGLE']

## MOCKUP

# Error when client is not found
MOCKUP_ERROR = 'Client could not be found. Please, try again.'

# Response when client is found
MOCKUP_RESPONSE = '<b>Client:</b> {client}\n<b>E-mail:</b> {email}\n<b>Phone:</b> {phone}'

## GOOGLE

# Response when speech-to-text was not found
GOOGLE_ERROR = 'Could not perform speech recognition. Please, try again.'

# Response when voice message is saved and waits for API call
GOOGLE_WAITING = 'Voice message received. Please, wait.'

# Response when transcript is found
GOOGLE_RESPONSE = '<b>Transcript:</b> {transcript}'

# Fallback

# Regex to capture user's fallback
FALLBACK_REGEX = '^(Terminate)$'

# Response when fallback.end is called
FALLBACK_END_RESPONSE = 'Session has been terminated. If you wish, please talk again with me.'

# Response when fallback.retry is called
FALLBACK_RETRY_RESPONSE = 'Do you need anything else?'
