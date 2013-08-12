from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.NewsListView.as_view(), name='rmc_news_list'),
)
