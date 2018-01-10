from __future__ import absolute_import

from django.contrib.auth.views import login
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url('', include('openeats.urls')),
]



if settings.SERVE_MEDIA:
    urlpatterns += [
        url(r'^site-media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
        ]

