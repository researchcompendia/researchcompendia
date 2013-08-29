from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from envelope.views import ContactView

from home.views import FaqView, HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='rmc_home'),
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
    url(r'^faq/', FaqView.as_view(), name='rmc_faq'),
    #url(r'^about/', AboutView.as_view(), name='rmc_about'),

    url(r'^news/', include('news.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^pages/', include('django.contrib.flatpages.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/', 'flatpage', {'url': '/about/'}, name='rmc_about'),
    url(r'^terms/', 'flatpage', {'url': '/terms/'}, name='rmc_terms'),
    url(r'^privacy/', 'flatpage', {'url': '/privacy/'}, name='rmc_privacy'),
)
