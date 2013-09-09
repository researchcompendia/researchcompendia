from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from . import views
from .forms import CompanionForm

urlpatterns = patterns('',
    url(r'/create/', TemplateView.as_view(template_name='supportingmaterials/create.html'), {'form_class':CompanionForm}, name='rmc_create'),
    url(r'^$', views.CompanionArticleListView.as_view(), name='rmc_companionpages'),
)
