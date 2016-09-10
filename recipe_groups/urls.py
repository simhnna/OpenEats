from __future__ import absolute_import

from django.conf.urls import *
from recipe_groups.views import CourseList, CuisineList, CuisineCreate, CuisineUpdate, CourseCreate, CourseUpdate, course_pop, course_recipes, cuisine_pop, cuisine_recipes
from .models import Course, Cuisine

course_info = {
                "queryset":Course.objects.all(),
                "template_object_name":"course",
            }
cuisine_info = {
                "queryset":Cuisine.objects.all(),
                "template_object_name": "cuisine",
             }

urlpatterns = [
    url(r'^popadd/course/$', course_pop),
    url(r'^course/$', CourseList.as_view(), name="course_list"),
    url(r'^course/new/$', CourseCreate.as_view(), name='course_add'),
    url(r'^course/(?P<slug>[-\w]+)/$', course_recipes, name="course_recipes"),
    url(r'^popadd/cuisine/$', cuisine_pop),
    url(r'^cuisine/$', CuisineList.as_view()),
    url(r'^cuisine/new/$', CuisineCreate.as_view(), name="cuisine_add"),
    url(r'^cuisine/(?P<slug>[-\w]+)/$', cuisine_recipes, name="cuisine_recipes"),
]
