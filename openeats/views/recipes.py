from __future__ import absolute_import

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles import finders
from django.forms.models import inlineformset_factory
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import ugettext as _
from django.views.generic import ListView

from openeats.forms.recipes import IngItemFormSet, RecipeForm
from openeats.models.ingredients import Ingredient
from openeats.models.recipes import Recipe

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer


def index(request):
    recipe_list = Recipe.objects.filter(shared=Recipe.SHARE_SHARED).order_by('-pub_date')[0:6]
    return render(request, 'openeats/index.html', {'new_recipes': recipe_list})


def recipeShow(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # setting the four previously viewed recipes in the user session
    # so they can be easily accessed on the sidebar
    if 'recipe_history' in request.session:
        sessionlist = request.session['recipe_history']
        if [recipe.title, recipe.get_absolute_url()] not in sessionlist:
            sessionlist.append(([recipe.title, recipe.get_absolute_url()]))
            if len(sessionlist) > 4:
                sessionlist.pop(0)
            request.session['recipe_history'] = sessionlist
    else:
        request.session['recipe_history'] = [[recipe.title, recipe.get_absolute_url()]]

    # check if the recipe is a private recipe if so through a 404 error
    if recipe.shared == Recipe.PRIVATE_SHARED and recipe.author != request.user:
        raise Http404(_("Recipe %s is marked Private") % recipe.title)
    else:
        return render(request, 'openeats/recipe_detail.html', {'recipe': recipe})


def recipePrint(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # check if the recipe is a private recipe if so through a 404 error
    if recipe.shared == Recipe.PRIVATE_SHARED and recipe.author != request.user:
        raise Http404(_('Recipe %s is marked Private') % recipe.title)
    else:
        return render(request, 'openeats/recipe_print.html', {'recipe': recipe})


@login_required
def recipe(request, user=None, pk=None):
    """used to create or edit a recipe"""
    IngFormSet = inlineformset_factory(Recipe, Ingredient,
                                       exclude=[], extra=5, formset=IngItemFormSet)

    if user and pk:  # must be editing a recipe
        recipe_inst = get_object_or_404(Recipe, author__username=request.user.username, pk=pk)
    else:
        recipe_inst = Recipe()

    if request.method == 'POST':
        form = RecipeForm(data=request.POST, files=request.FILES, instance=recipe_inst)
        formset = IngFormSet(request.POST, instance=recipe_inst)
        if form.is_valid() and formset.is_valid():
            new_recipe = form.save()
            instances = formset.save(commit=False)  # save the ingredients seperatly
            for instance in instances:
                # set the recipe id foregin key to the this recipe id
                instance.recipe_id = new_recipe.id
                instance.save()
            form.save(commit=False)
            return redirect(new_recipe.get_absolute_url())
    else:
        form = RecipeForm(instance=recipe_inst)

        # if we are editing an existing recipe disable the title field so it can't be changed
        if recipe_inst.id:
            form.fields['title'].widget.attrs['readonly'] = True

        formset = IngFormSet(instance=recipe_inst)
    return render(request, 'openeats/recipe_form.html', {'form': form, 'formset': formset, })


def recipeUser(request, shared, user):
    """Returns a list of recipes for a giving user
    if shared is set to share then it will show the shared recipes
    if it is set to private then only the private recipes will be shown
    this is mostly used for the users profile to display the users recipes
    """
    if shared == 'share':
        recipe_list = Recipe.objects.filter(author__username=user,
                                            shared=Recipe.SHARE_SHARED).order_by('-pub_date')
    else:
        recipe_list = Recipe.objects.filter(author__username=user,
                                            shared=Recipe.PRIVATE_SHARED).order_by('-pub_date')

    return render(request, 'openeats/recipe_userlist.html',
                  {'recipe_list': recipe_list, 'user': user, 'shared': shared})


def exportPDF(request, pk):
    """Exports recipes to a pdf"""

    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
    pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
    registerFontFamily('Vera', normal='Vera', bold='VeraBd', italic='VeraIt', boldItalic='VeraBI')

    recipe = get_object_or_404(Recipe, pk=pk)

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + recipe.title + '.pdf'

    # Our container for 'Flowable' objects
    elements = []

    # set up our styles
    styles = getSampleStyleSheet()
    styleH1 = styles['Heading1']
    styleH1.textColor = colors.green
    styleH1.fontName = 'VeraBd'
    styleH2 = styles['Heading2']
    styleH2.textColor = colors.goldenrod
    styleH2.fontName = 'Vera'
    styleNormal = styles['Normal']
    styleNormal.fontName = 'Vera'
    styleBullet = styles['Bullet']
    styleBullet.fontName = 'VeraIt'

    # create the pdf doc
    doc = SimpleDocTemplate(response)

    # set the openeats logo
    logo = Image(finders.find(settings.OELOGO))
    logo.hAlign = 'LEFT'
    elements.append(logo)
    elements.append(Spacer(0, 1 * cm))

    # add the recipe photo if the recipe has one
    if recipe.photo:
        photo = settings.BASE_PATH + recipe.photo.url
        image = Image(photo)
        image.height = "CENTER"
        elements.append(image)
        elements.append(Spacer(0, 0.5 * cm))

    # add the meat of the pdf
    elements.append(Paragraph(recipe.title, styleH1))
    elements.append(Paragraph('info', styleH2))
    elements.append(Paragraph(recipe.info, styleNormal))
    elements.append(Paragraph('ingredients', styleH2))

    for ing in recipe.ingredients.all():
        ing = "%s %s %s %s" % (ing.quantity, ing.measurement, ing.title, ing.preparation)
        elements.append(Paragraph(ing, styleBullet))

    elements.append(Paragraph('directions', styleH2))
    elements.append(Paragraph(recipe.directions, styleNormal))

    # build the pdf and return it
    doc.build(elements)
    return response


class RecentRecipeView(ListView):
    context_object_name = "recipe_list"
    queryset = Recipe.objects.filter(shared=Recipe.SHARE_SHARED).order_by('-pub_date', 'title')[:20]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RecentRecipeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Recent Recipes'
        return context
