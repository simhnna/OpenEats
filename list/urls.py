from __future__ import absolute_import

from django.conf.urls import *
from .views import index, groceryAddRecipe, groceryMail, groceryDelete, groceryAjaxDelete, groceryAisleAjaxDelete, groceryCreate, groceryShow, groceryShareList, groceryUnShareList, groceryProfile, groceryAisle

urlpatterns = [
    url(r'^grocery/$', index, name="grocery_list"),
    url(r'^grocery/recipe/(?P<recipe_slug>[-\w]+)/$', groceryAddRecipe, name='grocery_addrecipe'),
    url(r'^grocery/mail/(?P<gid>\d+)/$', groceryMail, name='grocery_mail'),
    url(r'^grocery/delete/(?P<id>\d+)/$', groceryDelete, name='grocery_delete'),
    url(r'^grocery/ajaxdelete/$', groceryAjaxDelete, name='grocery_Ajaxdelete'),
    url(r'^grocery/aisle/ajaxdelete/$', groceryAisleAjaxDelete, name="grocery_aisledelete"),
    url(r'^grocery/create/$', groceryCreate, name="grocery_create"),
    url(r'^grocery/edit/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', groceryCreate, name='grocery_edit'),
    url(r'^grocery/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', groceryShow, name='grocery_show'),
    url(r'^grocery/print/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', groceryShow, {'template_name':'list/grocery_print.html',}, name='grocery_print'),
    url(r'^grocery/share/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', groceryShareList, name='grocery_share'),
    url(r'^grocery/unshare/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', groceryUnShareList, name='grocery_unshare'),
    url(r'^grocery/grocery-ajax/$', groceryProfile, name="grocery_profile"),
    url(r'^grocery/aisle/$', groceryAisle, name="grocery_aisle"),
]
