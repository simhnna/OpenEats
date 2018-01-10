from django.db import models
from django.utils.translation import ugettext_lazy as _


class Course(models.Model):
    title = models.CharField(_('title'), max_length=100, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "course/%s" % self.pk

    def recipe_count(self):
        return self.recipe_set.filter(shared=0).count()


class Cuisine(models.Model):
    title = models.CharField(_('title'), max_length=100, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "cuisine/%s" % self.pk

    def recipe_count(self):
        return self.recipe_set.filter(shared=0).count()
