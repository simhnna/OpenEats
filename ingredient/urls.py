from  __future__ import absolute_import

from django.conf.urls import *
from .views import autocomplete_ing

urlpatterns = [
   url(r'^auto/$', autocomplete_ing),
]
