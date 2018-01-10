from django.conf.urls import include, url

from openeats.views.ingredients import autocomplete_ing
from openeats.views.recipe_groups import (CourseCreate, CourseList, CuisineCreate,
                                          CuisineList, course_pop, course_recipes,
                                          cuisine_pop, cuisine_recipes)
from openeats.views.recipes import (RecentRecipeView, exportPDF, index, recipe,
                                    recipePrint, recipeShow, recipeUser)
from openeats.views.tags import recipeTags


recipe_patterns = [
    url(r'^new/$', recipe, name="new_recipe"),
    url(r'^edit/(?P<user>[-\w]+)/(?P<pk>[\d]+)/$', recipe, name='recipe_edit'),
    url(r'^print/(?P<pk>[\d]+)/$', recipePrint, name="print_recipe"),
    url(r'^ajaxulist/(?P<shared>[-\w]+)/(?P<user>[-\w]+)/$', recipeUser),
    url(r'^recent/$', RecentRecipeView.as_view(), name='recipe_recent'),
    url(r'^(?P<pk>[\d]+)/$', recipeShow, name='recipe_show'),
    url(r'^export/(?P<pk>[\d]+)/$', exportPDF, name='recipe_export'),
    url(r'^$', index, name='recipe_index'),
]


recipe_group_patterns = [
    url(r'^popadd/course/$', course_pop, name='course_pop'),
    url(r'^course/$', CourseList.as_view(), name="course_list"),
    url(r'^course/new/$', CourseCreate.as_view(), name='course_add'),
    url(r'^course/(?P<pk>[\d]+)/$', course_recipes, name="course_recipes"),
    url(r'^popadd/cuisine/$', cuisine_pop, name='cuisine_pop'),
    url(r'^cuisine/$', CuisineList.as_view(), name='cuisine_list'),
    url(r'^cuisine/new/$', CuisineCreate.as_view(), name="cuisine_add"),
    url(r'^cuisine/(?P<pk>[\d]+)/$', cuisine_recipes, name="cuisine_recipes"),
]


ingredient_patterns = [
   url(r'^auto/$', autocomplete_ing, name='ingredient_autocomplete'),
]


tag_patterns = [
    url(r'^recipe/(?P<tag>[-\w]+)/$', recipeTags, name="recipe_tags"),
]

urlpatterns = [
    url(r'^groups/', include(recipe_group_patterns)),
    url(r'^recipe/', include(recipe_patterns)),
    url(r'^ingredient/', include(ingredient_patterns)),
    url(r'^tags/', include(tag_patterns)),
    url(r'^$', index),
]
