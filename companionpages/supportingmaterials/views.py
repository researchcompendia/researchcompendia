from django.views import generic

from .models import Article
from .forms import ArticleForm


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'supportingmaterials/index.html'
    context_object_name = 'companion_article_list'


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'supportingmaterials/detail.html'


class ArticleCreateView(generic.edit.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'supportingmaterials/create.html'
