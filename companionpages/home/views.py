from django.conf import settings
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic import TemplateView

from .models import Faq
from news.models import News
from supportingmaterials.models import CompanionArticle

class HomeView(TemplateView):
    template_name="base.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['newsbriefs_list'] = News.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:10]
        context['site_title'] = settings.SITE_TITLE
        context['companion_article_list'] = CompanionArticle.objects.all().order_by('-modified')[:10]
        return context

class FaqView(ListView):
    model = Faq
    context_object_name = 'faq_list'

    template_name='faq.html'

class AboutView(TemplateView):
    template_name="about.html"

class CompanionView(TemplateView):
    template_name="create.html"
