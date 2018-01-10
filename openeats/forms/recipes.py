from __future__ import absolute_import

from django import forms
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from openeats.models.recipe_groups import Course, Cuisine
from openeats.models.recipes import Recipe


class SelectWithPop(forms.Select):
    """
    Add's a link to a select box to popup a form to allow you to add new items
    to a select box via a form. You need to include the js RelatedObjectLookups
    on the main form
    """
    def render(self, name, * args, ** kwargs):
        html = super(SelectWithPop, self).render(name, * args, ** kwargs)
        popupplus = render_to_string("openeats/recipe_groups/popupplus.html", {'field': name})
        return html + popupplus


class RecipeForm(forms.ModelForm):
    """ Used to create new recipes the course and cuisine field are created with a
        speical widget that appends a link and graphic to the end of select field to allow
        users to add new items via a popup form
    """
    course = forms.ModelChoiceField(Course.objects, widget=SelectWithPop)
    cuisine = forms.ModelChoiceField(Cuisine.objects, widget=SelectWithPop)

    class Meta:
        model = Recipe
        exclude = ('ingredient',)


class IngItemFormSet(forms.models.BaseInlineFormSet):
    """Require at least two ingredient in the formset to be completed."""
    def clean(self):
        super(IngItemFormSet, self).clean()
        for error in self.errors:
            if error:
                return
        completed = 0
        for cleaned_data in self.cleaned_data:
            if cleaned_data and not cleaned_data.get('DELETE', False):
                completed += 1
        if completed < 2:
            raise forms.ValidationError(_('At least two %s are required.' %
                                          self.model._meta.object_name.lower()))
