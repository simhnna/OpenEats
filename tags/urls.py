from __future__ import absolute_import

from django.conf.urls import *
from .views import recipeTags

urlpatterns = [
    url(r'^recipe/(?P<tag>[-\w]+)/$', recipeTags, name="recipe_tags"),
]
