from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.CompanionArticleListView.as_view(), name='rmc_companionsites'),
)
