from django.utils import timezone
from django.views import generic

from .models import News


class NewsListView(generic.ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'recent_news_list'

    def get_queryset(self):
        """Return recently published newsbriefs"""
        return News.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:10]
