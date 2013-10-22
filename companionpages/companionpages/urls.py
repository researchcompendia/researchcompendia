from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from envelope.views import ContactView
from home.views import FaqView, HomeView
from members.forms import MemberForm

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='rmc_home'),
    url(r'^api/v1/', include('api.urls')),
    url(r'^members/edit', 'profiles.views.edit_profile', {'form_class': MemberForm, }, name='rmc_edit'),
    url(r'^members/', include('profiles.urls')),
    # profiles/create/ named profiles_create_profile
    # profiles/edit/ named profiles_edit_profile
    # profiles/username named profiles_profile_detail
    # profiles/ named profiles_profile_list
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', ContactView.as_view(template_name='contact.html'),
        name='envelope-contact'),
    url(r'^faq/', FaqView.as_view(), name='rmc_faq'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^compendia/', include('supportingmaterials.urls')),
)

urlpatterns += patterns(
    'django.contrib.flatpages.views',
    url(r'^about/', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^terms/', 'flatpage', {'url': '/terms/'}, name='terms'),
    url(r'^privacy/', 'flatpage', {'url': '/privacy/'}, name='privacy'),
    url(r'^partners/', 'flatpage', {'url': '/partners/'}, name='partners'),
    url(r'^developers/', 'flatpage', {'url': '/developers/'}, name='developers'),
)
