from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

from envelope.views import ContactView

from home.views import FaqView, HomeView
from members.forms import MemberForm
from supportingmaterials.forms import CompanionForm

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='rmc_home'),
    url(r'^members/edit', 'profiles.views.edit_profile', {'form_class': MemberForm,}, name='rmc_edit'),
    url(r'^members/', include('profiles.urls')),
    # profiles/create/ named profiles_create_profile
    # profiles/edit/ named profiles_edit_profile
    # profiles/username named profiles_profile_detail
    # profiles/ named profiles_profile_list
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', ContactView.as_view(template_name='contact.html'),
        name='envelope-contact'),
    url(r'^faq/', FaqView.as_view(), name='rmc_faq'),
    url(r'^news/', include('news.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^supportingmaterials/create', TemplateView.as_view(template_name='supportingmaterials/create.html'), {'form_class':CompanionForm}, name='rmc_create'),
    url(r'^supportingmaterials/', include('profiles.urls')),
=======
    url(r'^supportingmaterials/create', TemplateView.as_view(template_name='supportingmaterials/create.html'), name='rmc_create'),
    url(r'^companionsites', include('supportingmaterials.urls')),
>>>>>>> 9e0b123e4dc094ba619854c74cd5a0053e84dc8c
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/', 'flatpage', {'url': '/about/'}, name='rmc_about'),
    url(r'^terms/', 'flatpage', {'url': '/terms/'}, name='rmc_terms'),
    url(r'^privacy/', 'flatpage', {'url': '/privacy/'}, name='rmc_privacy'),
)
