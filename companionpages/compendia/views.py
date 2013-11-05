import logging
from django.conf import settings
from django.views import generic

from braces.views import FormMessagesMixin, LoginRequiredMixin

from .models import Article
from .forms import ArticleForm, DoiForm

logger = logging.getLogger(__name__)


class DoiFormView(generic.FormView):
    form_class = DoiForm
    template_name = 'compendia/doi.html'


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'compendia/index.html'
    paginate_by = 25

    def get_queryset(self):
        return Article.objects.filter(status__iexact=Article.STATUS.active)


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'compendia/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['static_url'] = settings.STATIC_URL.rstrip('/')
        return context


class ArticleCreateView(LoginRequiredMixin, FormMessagesMixin, generic.edit.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'compendia/create.html'
    form_invalid_message = 'The article was not created, and administrators have been notified.'

    def get_form_valid_message(self):
        return "Article '{0}' created!".format(self.object.title)
