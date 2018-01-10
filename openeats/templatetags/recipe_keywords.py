from django import template

from openeats.models.recipes import Recipe

register = template.Library()


@register.simple_tag
def recipe_keywords(recipe_id, tag_count):
    """Used to get the recipe tags from a recipe and make them keywords"""
    recipe = Recipe.objects.get(pk=recipe_id)
    keyword_list = []
    keyword_list.append(recipe.title)
    for tag in []:
        keyword_list.append(tag.name)
    keyword_string = ','.join(keyword_list[0:tag_count])
    return keyword_string

