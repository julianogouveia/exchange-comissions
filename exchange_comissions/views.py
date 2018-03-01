import importlib

from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from account.decorators import login_required

from exchange_core.views import SignupView
from exchange_core.models import Users
from exchange_comissions.models import Sponsorships


class SponsorshipView(SignupView):
    template_name = 'comissions/sponsorship.html'

    def dispatch(self, request, username):
        self.sponsor = Users.objects.get(username=username, is_active=True)
        return super().dispatch(request, username)

    def get_context_data(self, form=None):
        context = super().get_context_data()
        context['sponsor'] = self.sponsor
        context['sponsorships'] = Sponsorships.objects.filter(sponsor=self.request.user)
        return context

    def after_signup(self, form):
        super().after_signup(form)

        sponsorship = Sponsorships()
        sponsorship.sponsor = self.sponsor
        sponsorship.sponsored = self.created_user
        sponsorship.save()


@method_decorator([login_required], name='dispatch')
class DashboardView(TemplateView):
    template_name = 'comissions/dashboard.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['customers'] = Sponsorships.objects.filter(sponsor=self.request.user, sponsored__is_active=True)
        return context
        