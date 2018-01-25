from django.urls import re_path, path, include
from django.conf import settings

from . import views


urlpatterns = [
	path(settings.SPONSORSHIP_URL_PREFIX + '<username>/', views.SponsorshipView.as_view(), name='comissions>sponsorship'),
]