from django.conf import settings
from django.views.generic import ListView
from django.views.generic import TemplateView

from .models import Faq


class HomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['site_title'] = settings.SITE_TITLE
        return context


class FaqView(ListView):
    model = Faq
    context_object_name = 'faq_list'

    template_name = 'faq.html'
