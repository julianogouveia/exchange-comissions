from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
	name = 'exchange_comissions'
	verbose_name = _('Comissions')