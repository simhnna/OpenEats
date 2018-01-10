from django.conf.urls import *
from helpers.recipe_views import RecentRecipeView
from recipe.views import CookList, recipe, recipeMail, recipeNote, recipePrint, recipeReport, recipeUnStore, recipeStore, recipeUser, recipeUserFavs, recipeShow, exportPDF, index


urlpatterns = [
    url(r'^new/$', recipe, name="new_recipe"),
    url(r'^mail/(?P<id>\d+)/$', recipeMail, name='recipe_mail'),
    url(r'^edit/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', recipe, name='recipe_edit'),
    url(r'^print/(?P<slug>[-\w]+)/$', recipePrint, name="print_recipe"),
    url(r'^cook/(?P<slug>[-\w]+)/$', CookList.as_view()),
    url(r'^report/(?P<slug>[-\w]+)/$', recipeReport, name='recipe_report'),
    url(r'^store/(?P<object_id>\d+)/$', recipeStore, name='recipe_store'),
    url(r'^unstore/$', recipeUnStore, name='recipe_unstore'),
    url(r'^ajaxnote/$', recipeNote),
    url(r'^ajaxulist/(?P<shared>[-\w]+)/(?P<user>[-\w]+)/$', recipeUser),
    url(r'^ajax-favrecipe/$', recipeUserFavs),
    url(r'^recent/$', RecentRecipeView.as_view(), name='recipe_recent'),
    url(r'^(?P<slug>[-\w]+)/$', recipeShow, name='recipe_show'),
    url(r'^export/(?P<slug>[-\w]+)/$', exportPDF, name='recipe_export'),
    url(r'^$', index, name='recipe_index'),
]
