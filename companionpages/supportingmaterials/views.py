from django.views import generic

from .models import Article
from .models import SupportingMaterial
from .forms import ArticleForm
from .forms import SupportingMaterialForm


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


class SupplementalMaterialCreateView(generic.edit.CreateView):
    model = SupportingMaterial
    form_class = SupportingMaterialForm
    template_name = 'supportingmaterials/create.html'
