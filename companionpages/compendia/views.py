from datetime import datetime
import logging
from django.conf import settings
from django.contrib.sites.models import Site
from django.views import generic

from braces.views import FormMessagesMixin, LoginRequiredMixin

from .models import Article
from .forms import ArticleForm, ArticleUpdateForm

logger = logging.getLogger('researchcompendia.compendia')


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'compendia/index.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['static_url'] = settings.STATIC_URL.rstrip('/')
        context['domain'] = Site.objects.get_current().domain
        context['now'] = datetime.now()
        return context

    def get_queryset(self):
        return Article.objects.filter(status__iexact=Article.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'compendia/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['static_url'] = settings.STATIC_URL.rstrip('/')
        context['domain'] = Site.objects.get_current().domain
        context['now'] = datetime.now()
        return context


class ArticleCreateView(LoginRequiredMixin, FormMessagesMixin, generic.edit.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'compendia/create.html'

    def form_valid(self, form):
        form.instance.site_owner = self.request.user
        return super(ArticleCreateView, self).form_valid(form)

    def get_form_invalid_message(self):
        logger.error('An attempt to create an article has failed. USER: %s PATH: %s GET: %s POST: %s',
                self.request.user, self.request.path, self.request.GET, self.request.POST)
        return 'The article was not created, and the site administrators have been notified.'

    def get_form_valid_message(self):
        return "Article created!"


class ArticleUpdateView(LoginRequiredMixin, FormMessagesMixin, generic.UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'compendia/update.html'

    def get_form_invalid_message(self):
        logger.error('An attempt to update article %s has failed.', self.object.id)
        return "Article was not updated! The administrators have been notified."

    def get_form_valid_message(self):
        return "Article updated!"
