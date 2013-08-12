from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from envelope.views import ContactView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^profiles/', include('profiles.urls')),
    # profiles urls are
    # profiles/create/ named profiles_create_profile
    # profiles/edit/ named profiles_edit_profile
    # profiles/username named profiles_profile_detail
    # profiles/ named profiles_profile_list
    # I'm not sure I like using include('profiles.urls') since
    # I think it is not self documenting. it goes against
    # explicit over implicit. but I need to think about this.
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', ContactView.as_view(template_name='contact.html'),
        name='envelope-contact'),
    url(r'^news/', include('news.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
