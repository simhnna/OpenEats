from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Course(models.Model):
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)
    author = models.ForeignKey(User, verbose_name=_('author'))

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "course/self.slug"

    def recipe_count(self):
        return self.recipe_set.filter(shared=0).count()


@python_2_unicode_compatible
class Cuisine(models.Model):
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)
    author = models.ForeignKey(User, verbose_name=_('author'))

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "cuisine/self.slug"

    def recipe_count(self):
        return self.recipe_set.filter(shared=0).count()
