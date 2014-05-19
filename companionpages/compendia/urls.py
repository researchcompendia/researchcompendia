from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ArticleListView.as_view(), name='list'),
    url(r'^browse/(?P<compendium_type>.*)/$', views.ArticleTypeListView.as_view(), name='browse'),
    url(r'^b/$', views.ArticleBrowseView.as_view(), name='b'),
    url(r'^toc/$', views.TableOfContentsView.as_view(), name='toc'),
    url(r'^create/$', views.ArticleCreateView.as_view(), name='create'),
    url(r'^(?P<year>\d{4})\.(?P<pk>\d+)/$', views.ArticleYearView.as_view(), name='year_detail'),
    url(r'^(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='pk_detail'),
    url(r'^update/(?P<pk>\d+)/$', views.ArticleUpdateView.as_view(), name='update'),
)
