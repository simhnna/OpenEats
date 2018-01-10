from django.contrib import admin
from django.shortcuts import render_to_response

from openeats.forms.recipes import IngItemFormSet
from openeats.models.ingredients import Ingredient
from openeats.models.recipe_groups import Course, Cuisine
from openeats.models.recipes import Recipe


class RecipeInline(admin.TabularInline):
    model = Ingredient
    formset = IngItemFormSet


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    def export_MealMaster(self, request, queryset):
        response = render_to_response('recipe/mealmaster_export.txt',
                                      {'queryset': queryset}, mimetype='text/plain')
        response['Content-Disposition'] = 'attachment; filename=recipe.txt'
        return response

    export_MealMaster.short_description = "Export Meal Master"

    actions = [export_MealMaster]
    inlines = [RecipeInline]
    list_display = ['title', 'author', 'pub_date', 'shared']
    # admin_thumbnail = AdminThumbnail(image_field='photo')
    list_filter = ['shared', 'author', 'course', 'cuisine']
    search_fields = ['author__username', 'title']
    radio_fields = {"shared": admin.HORIZONTAL}


class StoredRecipeAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe']
    search_fields = ['user__username', 'recipe__title']
    list_filter = ['user']


class ReportedRecipeAdmin(admin.ModelAdmin):

    def remove_recipe(self, request, queryset):
        """removes a recipe that has been reported"""
        for obj in queryset:
            obj.recipe.delete()
        if queryset.count() == 1:
            message = "1 recipe was deleted"
        else:
            message = "%s recipes were deleted" % queryset.count()
        self.message_user(request, message)
        return None

    remove_recipe.short_description = "Remove selected Recipes"
    actions = ['remove_recipe']
    list_display = ['recipe', 'reported_by']
    search_fields = ['reported_by__username', 'recipe__title']
    list_filter = ['reported_by']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title', 'author']
    list_filter = ['author']


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title', 'author']
    list_filter = ['author']
