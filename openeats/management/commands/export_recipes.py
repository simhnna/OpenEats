from django.core.management.base import BaseCommand, CommandError
from recipe.models import Recipe
from django.template import loader

class Command(BaseCommand):
    help = 'Outputs OpenEat recipes in the meal master format'

    def handle(self, *args, **options):
        #get a list of all the recipes
        try:
            recipes = Recipe.objects.all()
        except IndexError:
            raise CommandError("Could not get a list of recipes check your database")

        template = loader.get_template('recipe/mealmaster_export.txt')
        print(template.render({'queryset':recipes}))
