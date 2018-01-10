from __future__ import absolute_import

from django.forms import ModelForm

from openeats.models.recipe_groups import Course, Cuisine


class CoursePopForm(ModelForm):
    """form object for the popup from the recipe_form to add a new course"""
    class Meta:
        model = Course
        exclude = ('slug',)


class CuisinePopForm(ModelForm):
    """form object for the popup from the recipe_form to add a new cuisine"""
    class Meta:
        model = Cuisine
        exclude = ('slug',)
