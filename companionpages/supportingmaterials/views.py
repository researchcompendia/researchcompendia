import logging

from django.views import generic

from .models import Article
from .forms import ArticleForm, DoiForm

logger = logging.getLogger(__name__)


class DoiFormView(generic.FormView):
    form_class = DoiForm
    template_name = 'supportingmaterials/doi.html'


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


def get_author_names(compendia):
    """ helper function to join up author names from the doi_response """
    collaborators = compendia.setdefault('collaborators', [])
    authors = []
    for c in collaborators:
        name = '{first} {last}'.format(first=c.setdefault('given_name', ''), last=c.setdefault('surname'))
        authors.append(name)
    return ', '.join(authors)
