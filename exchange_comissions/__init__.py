from django.conf import settings
from prettyconf.configuration import Configuration

# Diz ao pretty conf o path do .env caso não existam variáveis de ambiente para a respectiva config
config = Configuration(starting_path=settings.BASE_DIR)

# Define o nome do modulo
PACKAGE_NAME = 'exchange_comissions'

# Diz ao Django aonde está a configuração desse modulo
default_app_config = PACKAGE_NAME + '.apps.Config'

# Define o prefixo da URL de patrocinio
settings.SPONSORSHIP_URL_PREFIX = config('SPONSORSHIP_URL_PREFIX', default='s/')

# Mostra os dados do patrocionador na pagina de cadastro por indicacao
settings.SPONSORSHIP_SHOW_DATA_ON_SINGUP = config('SPONSORSHIP_SHOW_DATA_ON_SINGUP', default=True, cast=config.boolean)

# Adiciona as variaveis de contexto ao template
settings.TEMPLATES[0]['OPTIONS']['context_processors'] += [
    '{}.context_processors.exchange'.format(PACKAGE_NAME),
]