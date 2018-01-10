from django.views.generic import ListView
from recipe.models import Recipe

class RecentRecipeView(ListView):
    context_object_name = "recipe_list"
    queryset=Recipe.objects.filter(shared=Recipe.SHARE_SHARED).order_by('-pub_date', 'title')[:20]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RecentRecipeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Recent Recipes'
        context['feed'] = "/feed/recent/"
        return context
