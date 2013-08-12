from django.utils import timezone
from django.views.generic import TemplateView

from news.models import News

class HomeView(TemplateView):
    template_name="base.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['newsbriefs_list'] = News.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:10]
        return context
