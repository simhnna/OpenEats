from django.core.management.base import BaseCommand, CommandError
from django.template import loader

from openeats.models.recipes import Recipe


class Command(BaseCommand):
    help = 'Outputs OpenEat recipes in the meal master format'

    def handle(self, *args, **options):
        try:
            recipes = Recipe.objects.all()
        except IndexError:
            raise CommandError("Could not get a list of recipes check your database")

        template = loader.get_template('recipe/mealmaster_export.txt')
        print(template.render({'queryset': recipes}))
