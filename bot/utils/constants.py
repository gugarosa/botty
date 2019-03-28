# encoding: utf-8

# Entry
# Regex to initiate bot flow (entry.options)
ENTRY_REGEX = '^(Oi|Olá|Ola|Ei|Bot)$'

# List of options provided by entry.options 
ENTRY_OPTIONS = [['Perfil do Cliente', 'Ocorrências', 'Sugestões', 'Finalizar']]

# Response provided by entry.options
ENTRY_OPTIONS_RESPONSE = 'Olá {name}! Por favor, escolha alguma opção.'

# Return state provided by entry.options
ENTRY_OPTIONS_STATE = 'AWAIT_OPTIONS'

# States
# Regex to capture user's chosen option
AWAIT_OPTIONS_REGEX = '^(Perfil do Cliente|Ocorrências|Sugestões)$'


# Fallback
# Regex to capture user's fallback
FALLBACK_REGEX = '^(Finalizar)$'

#
FALLBACK_END_RESPONSE = 'A sessão foi finalizada. Quando precisar, é só voltar a falar comigo.'