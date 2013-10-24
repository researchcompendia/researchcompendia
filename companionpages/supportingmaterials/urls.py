from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ArticleListView.as_view(), name='researchcompendia'),
    url(r'^create/$', views.ArticleCreateView.as_view(), name='researchcompendia_creation'),
    url(r'^(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='researchcompendium'),
    url(r'^doi/$', views.DoiFormView.as_view(), name='doifill'),
)
