from django.conf.urls import patterns, include, url
from django.contrib import admin

from metlabs.blog.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^events/', include('metlabs.events.urls')),
    url(r'^blog/', include('metlabs.blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markitup/', include('markitup.urls'))
)
