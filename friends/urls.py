from __future__ import absolute_import

from django.conf.urls import *
from .views import follow_list, feed

urlpatterns = [
    url(r'^following/(?P<username>[\w-]+)/$', follow_list, name="friends_following"),
    url(r'^feed/(?P<username>[\w-]+)/$', feed, name="friends_feed"),
]
