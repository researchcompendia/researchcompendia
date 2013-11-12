from django.views.generic import ListView

from .models import Faq


class FaqView(ListView):
    model = Faq
    context_object_name = 'faq_list'

    template_name = 'faq.html'
