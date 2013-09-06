from django.views import generic
from .models import CompanionArticle

class CompanionArticleListView(generic.ListView):
    model = CompanionArticle
    template_name = 'supportingmaterials/index.html'
    context_object_name = 'companion_article_list'
