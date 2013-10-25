import logging
from django.conf import settings
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
    paginate_by = 25

    def get_queryset(self):
        """Return active compendia"""
        return Article.objects.filter(status__iexact=Article.STATUS.active)


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'supportingmaterials/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['static_url'] = settings.STATIC_URL.rstrip('/')
        return context


class ArticleCreateView(generic.edit.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'supportingmaterials/create.html'


def get_author_names(compendia):
    """ helper function to join up author names from the doi_response """
    collaborators = compendia.get('collaborators', [])
    authors = []
    for c in collaborators:
        name = '{first} {last}'.format(first=c.get('given_name', ''), last=c.get('surname', ''))
        authors.append(name)
    return ', '.join(authors)
