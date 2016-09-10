from __future__ import absolute_import

from django.conf.urls import *
from .views import RecentRecipesFeed,TopRecipesFeed

urlpatterns = [
    url(r'^recent/$', RecentRecipesFeed()),
    url(r'^top/$', TopRecipesFeed()),
]
