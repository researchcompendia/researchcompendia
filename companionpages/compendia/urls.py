from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ArticleListView.as_view(), name='list'),
    url(r'^create/$', views.ArticleCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', views.ArticleUpdateView.as_view(), name='update'),
)
