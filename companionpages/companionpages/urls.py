from django.conf.urls import patterns, include, url
from django.contrib import admin

from compendia.views import ArticleDetailView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include('api.urls')),
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^compendia/', include('compendia.urls', namespace="compendia")),
    url(r'^search/', include('haystack.urls')),
    url(r'^markitup/', include('markitup.urls')),
    # don't ask some urls got listed in a grant with this url scheme. it can never break.
    url(r'^2013-11/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='bitterlegacy'),
    url(r'^', include('home.urls', namespace="home")),
)

urlpatterns += patterns(
    'django.contrib.flatpages.views',
    url(r'^terms/', 'flatpage', {'url': '/terms/'}, name='terms'),
    url(r'^privacy/', 'flatpage', {'url': '/privacy/'}, name='privacy'),
    url(r'^resources/', 'flatpage', {'url': '/resources/'}, name='resources'),
)
