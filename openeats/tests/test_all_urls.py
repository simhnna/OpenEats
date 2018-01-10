from django.urls import reverse
from django.test import TestCase

from django.contrib.auth.models import User

class URLTest(TestCase):
    fixtures = ['test_user_data.json', 'course_data.json', 'cuisine_data.json',
                'recipe_data.json', 'ing_data.json']

    def setUp(self):
        self.client.force_login(User.objects.first())

    def test_recipe_new(self):
        response = self.client.get(reverse('new_recipe'))
        self.assertEquals(response.status_code, 200)

    def test_recipe_edit(self):
        response = self.client.get(reverse('recipe_edit', args=[1, 1]))
        self.assertEquals(response.status_code, 200)

    def test_recipe_print(self):
        response = self.client.get(reverse('print_recipe', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_recent_recipes(self):
        response = self.client.get(reverse('recipe_recent'))
        self.assertEquals(response.status_code, 200)

    def test_recipe_show(self):
        response = self.client.get(reverse('recipe_show', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_recipe_export(self):
        response = self.client.get(reverse('recipe_export', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_recipe_index(self):
        response = self.client.get(reverse('recipe_index'))
        self.assertEquals(response.status_code, 200)

    def test_course_pop(self):
        response = self.client.get(reverse('course_pop'))
        self.assertEquals(response.status_code, 200)

    def test_course_list(self):
        response = self.client.get(reverse('course_list'))
        self.assertEquals(response.status_code, 200)

    def test_course_add(self):
        response = self.client.get(reverse('course_add'))
        self.assertEquals(response.status_code, 200)

    def test_course_recipes(self):
        response = self.client.get(reverse('course_recipes', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_cuisine_pop(self):
        response = self.client.get(reverse('cuisine_pop'))
        self.assertEquals(response.status_code, 200)

    def test_cuisine_list(self):
        response = self.client.get(reverse('cuisine_list'))
        self.assertEquals(response.status_code, 200)

    def test_cuisine_add(self):
        response = self.client.get(reverse('cuisine_add'))
        self.assertEquals(response.status_code, 200)

    def test_cuisine_recipes(self):
        response = self.client.get(reverse('cuisine_recipes', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_ingredient_autocomplete(self):
        response = self.client.get(reverse('ingredient_autocomplete'))
        self.assertEquals(response.status_code, 200)
