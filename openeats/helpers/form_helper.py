from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape


def handlePopAdd(request, addForm, field):
    """'This form helper is a pop up on the recipe form
    that allows users to add courses and cuisnes to the database, it returns
    the created object as the selected object on the recipe form"""

    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            try:
                newObject = form.save()
            except forms.ValidationError as error:
                newObject = None
            if newObject:
                return HttpResponse(
                    '<script type="text/javascript">'
                    'opener.dismissAddAnotherPopup(window, "%s", "%s");</script>' %
                    (escape(newObject._get_pk_val()), escape(newObject)))
    else:
        form = addForm()

    pageContext = {'form': form, 'field': field}
    return render(request, 'openeats/popadd.html', pageContext)
