from django.shortcuts import render, get_object_or_404


def recipeTags(request, tag):
    """displays a list of recipes with a giving tag"""
    recipe_tag = None #get_object_or_404(Tag, slug=tag)
    recipes_tagged = None #TaggedItem.objects.filter(tag=recipe_tag)
    recipe_list = []
    for recipe in recipes_tagged:
        recipe_list.append(recipe.content_object)

    return render(request, 'tags/recipe_tags.html', {'recipe_list': recipe_list})
