from django.conf import settings


def exchange(request):
	return {
		'SPONSORSHIP_URL_PREFIX': settings.SPONSORSHIP_URL_PREFIX
	}