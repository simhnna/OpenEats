from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from openeats.forms.recipe_groups import CoursePopForm, CuisinePopForm
from openeats.helpers.form_helper import handlePopAdd
from openeats.models.recipe_groups import Course, Cuisine
from openeats.models.recipes import Recipe


def course_recipes(request, pk):
    """Rectrives the recipe objects in a list that belong to the course passed to the method"""
    course_object = get_object_or_404(Course, pk=pk)
    recipe_list = course_object.recipe_set.filter(shared=Recipe.SHARE_SHARED)

    return render(request, 'recipe_groups/recipe_list.html',
                  {'recipe_list': recipe_list, 'category': course_object.title})


def cuisine_recipes(request, pk):
    """Retrives the recipe objects in a list that belong to the cuisine passed to the method"""
    cuisine_object = get_object_or_404(Cuisine, pk=pk)
    recipe_list = cuisine_object.recipe_set.filter(shared=Recipe.SHARE_SHARED)

    return render(request, 'recipe_groups/recipe_list.html',
                  {'recipe_list': recipe_list, 'category': cuisine_object.title})


@login_required
def course_pop(request):
    """Is called via js from the recipe form to allow users to add a new course
    with out leaving the recipe form"""
    return handlePopAdd(request, CoursePopForm, 'course')


@login_required
def cuisine_pop(request):
    """Is called via js from the recipe form to allow users to add a new cuisine
    with out leaving the recipe form"""
    return handlePopAdd(request, CuisinePopForm, 'cuisine')


class CourseList(ListView):
    context_object_name = 'course'
    template_name = 'openeats/recipe_groups/course_list.html'
    queryset = Course.objects.all()


class CuisineList(ListView):
    context_object_name = 'cuisine'
    queryset = Cuisine.objects.all()


class CourseCreate(CreateView):
    model = Course
    success_url = reverse_lazy('course_list')
    template_name = 'openeats/recipe_groups/course_form.html'
    fields = ['title']


class CourseUpdate(UpdateView):
    model = Course


class CuisineCreate(CreateView):
    model = Cuisine
    template_name = 'openeats/recipe_groups/course_form.html'
    success_url = reverse_lazy('recipe')


class CuisineUpdate(UpdateView):
    model = Cuisine
