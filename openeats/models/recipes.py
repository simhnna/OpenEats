from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from openeats.models.recipe_groups import Course, Cuisine


class Recipe(models.Model):
    SHARE_SHARED = 0
    PRIVATE_SHARED = 1
    SHARED_CHOCIES = (
        (SHARE_SHARED, _('Share')),
        (PRIVATE_SHARED, _('Private')),
    )

    title = models.CharField(_("Recipe Title"), max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    photo = models.ImageField(_('photo'), blank=True, upload_to="upload/recipe_photos")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('course'))
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, verbose_name=_('cuisine'))
    info = models.TextField(_('info'), help_text="enter information about the recipe")
    cook_time = models.IntegerField(_('cook time'), help_text="enter time in minutes")
    servings = models.IntegerField(_('servings'), help_text="enter total number of servings")
    directions = models.TextField(_('directions'))
    shared = models.IntegerField(_('shared'), choices=SHARED_CHOCIES, default=SHARE_SHARED,
                                 help_text="share the recipe with the community or mark it private")
    # tags = TaggableManager(_('tags'), help_text="separate with commas", blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['pub_date', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/recipe/%s/" % self.pk
