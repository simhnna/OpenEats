from __future__ import absolute_import

from django.conf.urls import *

from .views import index, entry
urlpatterns = [
    url(r'^list/$', index, name="news_list"),
    url(r'^entry/(?P<slug>[\w-]+)/$', entry, name="news_entry"),
]
