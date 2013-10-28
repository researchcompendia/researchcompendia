from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

from envelope.views import ContactView
from home.views import FaqView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='home'),
    url(r'^api/v1/', include('api.urls')),

    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),

    url(r'^contact/', ContactView.as_view(template_name='contact.html'),
        name='envelope-contact'),
    url(r'^faq/', FaqView.as_view(), name='faq'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^compendia/', include('compendia.urls')),
)

urlpatterns += patterns(
    'django.contrib.flatpages.views',
    # hard coded flatpages so that we can reference them with the url template tag
    url(r'^about/', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^terms/', 'flatpage', {'url': '/terms/'}, name='terms'),
    url(r'^privacy/', 'flatpage', {'url': '/privacy/'}, name='privacy'),
    url(r'^partners/', 'flatpage', {'url': '/partners/'}, name='partners'),
    url(r'^developers/', 'flatpage', {'url': '/developers/'}, name='developers'),
    # catchall pattern for when you don't want to use the url template tag for some reason
    url(r'^(?P<url>.*/)$', 'flatpage'),
)
