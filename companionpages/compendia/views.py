from datetime import datetime
import logging
from django.conf import settings
from django.contrib.sites.models import Site
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views import generic

from braces.views import FormMessagesMixin, LoginRequiredMixin
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView

from .models import Article, TableOfContentsOption
from .forms import ArticleForm, ArticleUpdateForm
from . import choices

logger = logging.getLogger('researchcompendia.compendia')


class ArticleFacetedSearchView(FacetedSearchView):
    def __init__(self, *args, **kwargs):
        super(ArticleFacetedSearchView, self).__init__(*args, **kwargs)

    def extra_context(self):
        extra = super(ArticleFacetedSearchView, self).extra_context()
        extra['compendium_type_lookup'] = choices.ENTRY_TYPE_LOOKUP
        extra['research_field_lookup'] = choices.RESEARCH_FIELD_LOOKUP
        return extra


class TableOfContentsView(generic.ListView):
    model = TableOfContentsOption
    template_name = 'asa.html'


class ArticleBrowseView(generic.base.TemplateView):
    template_name = 'compendia/browse.html'
    sqs = SearchQuerySet().facet('compendium_type').facet('primary_research_field')

    def get_context_data(self, **kwargs):
        context = super(ArticleBrowseView, self).get_context_data(**kwargs)
        context['searchqueryset'] = self.sqs
        context['facets'] = self.sqs.facet_counts()
        context['result_groups'] = self.make_facet_groups(self.sqs)
        context['compendium_type_lookup'] = choices.ENTRY_TYPE_LOOKUP
        context['research_field_lookup'] = choices.RESEARCH_FIELD_LOOKUP
        return context

    def make_facet_groups(self, sqs):
        counts = sqs.facet_counts()
        fields = counts.get('fields', {})
        type_counts = fields.get('compendium_type', [])
        facetgroups = []
        for compendium_type, count in type_counts:
            if compendium_type == '':
                continue
            items = self.sqs.filter(compendium_type=compendium_type).values(
                'pk',
                'title',
                'authors_text',
                'code_data_abstract',
                'journal',
            )
            facetgroups.append([compendium_type, [item for item in items][:5]])
        return facetgroups


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'compendia/index.html'
    paginate_by = 25
    sqs = SearchQuerySet().facet('compendium_type').facet('primary_research_field')

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['facets'] = self.sqs.facet_counts()
        context['static_url'] = settings.STATIC_URL.rstrip('/')
        context['media_url'] = settings.MEDIA_URL
        context['domain'] = Site.objects.get_current().domain
        context['now'] = datetime.now()
        context['compendium_type_lookup'] = choices.ENTRY_TYPE_LOOKUP
        context['research_field_lookup'] = choices.RESEARCH_FIELD_LOOKUP
        return context

    def get_queryset(self):
        return Article.objects.filter(status__iexact=Article.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)


class ArticleTypeListView(ArticleListView):
    template_name = 'compendia/title_list.html'

    def get_queryset(self):
        compendium_type = self.kwargs.get('compendium_type', None)
        return Article.objects.filter(status__iexact=Article.STATUS.active).filter(compendium_type=compendium_type)


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'compendia/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['static_url'] = settings.STATIC_URL.rstrip('/')
        context['media_url'] = settings.MEDIA_URL
        context['domain'] = Site.objects.get_current().domain
        context['now'] = datetime.now()
        verifications = self.object.verification_set.all()[:5]
        context['recent_verifications'] = verifications
        context['compendium_type_lookup'] = choices.ENTRY_TYPE_LOOKUP
        context['research_field_lookup'] = choices.RESEARCH_FIELD_LOOKUP
        return context


class ArticleYearView(ArticleDetailView):
    year_url_kwarg = 'year'

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        Raises a 404 if the `year` in the url does not match the created year of the object.

        This requires a `pk` and `year` argument in the URLconf
        """
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        year = self.kwargs.get(self.year_url_kwarg, None)

        if pk is None or year is None:
            raise AttributeError("%s must be called with an object pk and a year."
                                 % self.__class__.__name__)

        queryset = queryset.filter(pk=pk)
        try:
            article = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})

        # Next, check that the created year matches
        year_created = article.created.strftime('%Y')
        if year_created != year:
            raise Http404(_("%(verbose_name)s %(pk)s not found in year %(year)s. Did you mean %(year_created)s?") % {
                'pk': pk,
                'verbose_name': queryset.model._meta.verbose_name,
                'year': year,
                'year_created': year_created,
            })

        return article


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
