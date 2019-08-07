# encoding: utf-8

# Entry

# Regex to initiate bot flow (entry.options)
ENTRY_REGEX = '^(?i)(Oi|Olá|Ola|Ei|Bot)'

# List of options provided by entry.options
ENTRY_OPTIONS = ['Perfil do Cliente', 'Pedido por Voz', 'Sugestões', 'Finalizar']

# Response provided by entry.options
ENTRY_OPTIONS_RESPONSE = 'Olá {name}! Acredita que hoje está {temperature} graus? Por favor, escolha alguma opção.'

# Response provided by entry.options with no location position
ENTRY_OPTIONS_RESPONSE_NO_LOCATION = 'Olá {name}! Notei que você ainda não me mandou sua localização. Por favor, escolha alguma opção ou me mande sua localização.'

# Reminder when user has not chosen an option
ENTRY_REMINDER = 'Ainda estou agurdando a sua opção.'

# States

## AWAIT_OPTIONS

# Regex to capture user's chosen option (order must match ENTRY_OPTIONS)
AWAIT_OPTIONS_REGEX = '^(Perfil do Cliente|Pedido por Voz|Sugestões)$'

# Responses according to possible options (order must match ENTRY_OPTIONS)
AWAIT_OPTIONS_RESPONSES = ['Por favor, digite o nome do cliente.',
                           'Por favor, envie uma mensagem de voz.', 'Por favor, envie o nome de um produto.']

# States according to possible options (order must match ENTRY_OPTIONS)
AWAIT_OPTIONS_STATES = ['CLIENT', 'INCIDENCE', 'SUGGESTION']

## CLIENT

# Error when client is not found
CLIENT_ERROR = 'Não foi possível encontrar o cliente. Por favor, tente novamente.'

# Response when client is found
CLIENT_RESPONSE = '<b>Cliente:</b> {client}\n<b>E-mail:</b> {email}\n<b>Telefone:</b> {phone}'

## INCIDENCE

# Response when speech-to-text was not found
INCIDENCE_ERROR = 'Não foi possível realizar a transcrição do áudio. Por favor, tente novamente.'

# Response when voice message is saved and waits for API call
INCIDENCE_WAITING = 'Mensagem de voz recebida. Por favor, aguarde um momento.'

# Response when transcript is found
INCIDENCE_RESPONSE = '<b>Transcrição:</b> {transcript}'

# Response when NER is found
INCIDENCE_RESPONSE_NER = '<b>Dados:</b> {ner}'

# Response when PORTAL is found
INCIDENCE_WAITING_PORTAL = 'Por favor, aguarde enquanto processamos seu pedido.'

## SUGGESTION

# Error when product is not found
SUGGESTION_ERROR = 'Não foi possível encontrar o produto. Por favor, tente novamente.'

# Response when product is found
SUGGESTION_RESPONSE = 'O produto <b>{product}</b> pertence à empresa <b>{company}</b> e está custando <b>R$ {price}</b>.'

# Fallback

# Regex to capture user's fallback
FALLBACK_REGEX = '^(Finalizar)$'

# Response when fallback.end is called
FALLBACK_END_RESPONSE = 'A sessão foi finalizada. Quando precisar, é só voltar a falar comigo.'

# Response when fallback.retry is called
FALLBACK_RETRY_RESPONSE = 'Você deseja mais alguma coisa?'
