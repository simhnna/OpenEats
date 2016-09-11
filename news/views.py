from __future__ import absolute_import

from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .models import Entry


def entry(request, slug):
    """returns one news entry"""
    entry = get_object_or_404(Entry, slug=slug)
    return render(request, 'news/entry.html', {'entry': entry})


def index(request):
    """returns a list of news stories"""
    entry_list = Entry.objects.all().order_by('pub_date')
    return render('news/entry_list.html', {'entry_list': entry_list})
