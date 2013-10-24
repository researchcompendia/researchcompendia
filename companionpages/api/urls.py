from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^s3/signatures', views.s3signatures, name='s3sign'),
    url(r'^dois', views.doi_crossref, name='doiref'),
)
