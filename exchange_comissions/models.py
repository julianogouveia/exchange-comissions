from django.db import models
from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from exchange_core.models import BaseModel
from model_utils.models import TimeStampedModel


class Sponsorships(TimeStampedModel, BaseModel):
	sponsor = models.ForeignKey('exchange_core.Users', related_name='sponsors', on_delete=models.CASCADE)
	sponsored = models.OneToOneField('exchange_core.Users', related_name='sponsored', on_delete=models.CASCADE)

