from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from envelope.views import ContactView
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='base'),
    url(r'^partners/', TemplateView.as_view(template_name="partners.html"), name='partners'),
    url(r'^about/', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^faq/', views.FaqView.as_view(), name='faq'),
    url(r'^contact/', ContactView.as_view(template_name='contact.html'), name='contact'),
    url(r'^developers/', ContactView.as_view(template_name='developers.html'), name='developers'),
)
