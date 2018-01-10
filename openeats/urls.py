from django.conf.urls import url, include

from openeats.views.recipes import recipe, recipePrint, recipeUser, recipeShow, exportPDF, index, RecentRecipeView


recipe_patterns = [
    url(r'^new/$', recipe, name="new_recipe"),
    url(r'^edit/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', recipe, name='recipe_edit'),
    url(r'^print/(?P<slug>[-\w]+)/$', recipePrint, name="print_recipe"),
    url(r'^ajaxulist/(?P<shared>[-\w]+)/(?P<user>[-\w]+)/$', recipeUser),
    url(r'^recent/$', RecentRecipeView.as_view(), name='recipe_recent'),
    url(r'^(?P<slug>[-\w]+)/$', recipeShow, name='recipe_show'),
    url(r'^export/(?P<slug>[-\w]+)/$', exportPDF, name='recipe_export'),
    url(r'^$', index, name='recipe_index'),
]


from openeats.views.recipe_groups import CourseList, CuisineList, CuisineCreate, CuisineUpdate, CourseCreate, CourseUpdate, course_pop, course_recipes, cuisine_pop, cuisine_recipes
from openeats.models.recipe_groups import Course, Cuisine

course_info = {
                "queryset":Course.objects.all(),
                "template_object_name":"course",
            }
cuisine_info = {
                "queryset":Cuisine.objects.all(),
                "template_object_name": "cuisine",
             }

recipe_group_patterns = [
    url(r'^popadd/course/$', course_pop),
    url(r'^course/$', CourseList.as_view(), name="course_list"),
    url(r'^course/new/$', CourseCreate.as_view(), name='course_add'),
    url(r'^course/(?P<slug>[-\w]+)/$', course_recipes, name="course_recipes"),
    url(r'^popadd/cuisine/$', cuisine_pop),
    url(r'^cuisine/$', CuisineList.as_view()),
    url(r'^cuisine/new/$', CuisineCreate.as_view(), name="cuisine_add"),
    url(r'^cuisine/(?P<slug>[-\w]+)/$', cuisine_recipes, name="cuisine_recipes"),
]


from openeats.views.ingredients import autocomplete_ing

ingredient_patterns = [
   url(r'^auto/$', autocomplete_ing),
]


from openeats.views.tags import recipeTags

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





