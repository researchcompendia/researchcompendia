from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
# from django.views.generic import TemplateView

from flatblocks.views import edit
from haystack.query import SearchQuerySet

from compendia.views import ArticleDetailView
from compendia.views import ArticleFacetedSearchView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include('api.urls')),
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^compendia/', include('compendia.urls', namespace="compendia")),
    # url(r'^search/', include('haystack.urls')),
    url(r'^markitup/', include('markitup.urls')),
    # TODO I'd like a flatblocks edit view that can take a slug
    url(r'^flatblocks/(?P<pk>\d+)/edit/$', staff_member_required(edit), name='flatblocks-edit'),
    # url(r'^asa/', TemplateView.as_view(template_name='asa.html'), name='asa_portal'),
    # don't ask some urls got listed in a grant with this url scheme. it can never break.
    url(r'^2013-11/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='bitterlegacy'),
    url(r'^', include('home.urls', namespace="home")),
)

sqs = SearchQuerySet().facet('compendium_type').facet('primary_research_field')
urlpatterns += patterns('haystack.views',
    url(r'^search/', ArticleFacetedSearchView(searchqueryset=sqs), name='haystack_search'),
)

urlpatterns += patterns(
    'django.contrib.flatpages.views',
    url(r'^terms/', 'flatpage', {'url': '/terms/'}, name='terms'),
    url(r'^privacy/', 'flatpage', {'url': '/privacy/'}, name='privacy'),
    url(r'^resources/', 'flatpage', {'url': '/resources/'}, name='resources'),
)
