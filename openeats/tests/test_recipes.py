from unittest import expectedFailure

from django.core.urlresolvers import reverse

from django_webtest import WebTest

from openeats.models.recipes import Recipe


class recipeViewsTestCase(WebTest):
    fixtures = ['test_user_data.json', 'course_data.json', 'cuisine_data.json',
                'recipe_data.json', 'ing_data.json']
    extra_environ = {'REMOTE_ADDR': '127.0.0.1'}
    csrf_checks = False

    @expectedFailure
    def test_redirect(self):
        """test that if a user is not logged in and they try to create a recipe
        they are sent to the login page"""
        resp = self.client.get(reverse('new_recipe'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/accounts/login/?next=' + reverse('new_recipe'))

    def test_detail(self):
        """test that you can access a recipe detail page"""
        recipe = Recipe.objects.get(pk=1)
        resp = self.client.get(reverse('recipe_show', kwargs={'pk': recipe.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('recipe' in resp.context)
        ing = recipe.ingredients.all()
        self.assertTrue(ing[0], 'black pepper')

    def test_bogus_url(self):
        resp = self.client.get(reverse('recipe_show', kwargs={'pk': '123124'}))
        self.assertEqual(resp.status_code, 404)

    def test_create(self):
        """test the creation of a recipe using the form"""
        resp = self.app.get(reverse('new_recipe'), user='testUser')
        self.assertEqual(resp.status_code, 200)
        form = resp.forms[1]
        form['title'] = 'my recipe'
        form['course'] = '1'
        form['cuisine'] = '2'
        form['info'] = "this is my recipe"
        form['cook_time'] = '20'
        form['servings'] = '2'
        form['shared'] = '1'  # making the recipe private
        # form['tags'] = 'recipe'
        form['directions'] = "cook till done"
        form['ingredients-0-quantity'] = '2'
        form['ingredients-0-measurement'] = 'cups'
        form['ingredients-0-title'] = 'flour'
        form['ingredients-1-quantity'] = '1'
        form['ingredients-1-measurement'] = 'cup'
        form['ingredients-1-title'] = 'water'
        resp = form.submit().follow()
        self.assertEqual(resp.context['recipe'].title, 'my recipe')
        recipe = Recipe.objects.get(pk=resp.context['recipe'].pk)
        self.assertTrue(recipe)

    def test_private(self):
        """makes sure only the owner of a private recipe can view it"""

        # sanity check make sure the recipe is private
        # call the create recipe test from above to load the DB with a private recipe
        self.test_create()
        recipe = Recipe.objects.get(title="my recipe")
        self.assertEqual(recipe.shared, 1)

        resp = self.app.get(reverse('recipe_show', kwargs={'pk': recipe.pk}),
                            user='testUser2', status=404)
        self.assertEqual(resp.status_code, 404)

        # test that the owner of the recipe can access it
        resp = self.app.get(reverse('recipe_show', kwargs={'pk': recipe.pk}), user='testUser')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['recipe'].title, 'my recipe')

    def test_print(self):
        """test the print view comes up"""
        recipe = Recipe.objects.get(pk=1)
        resp = self.client.get(reverse('print_recipe', kwargs={'pk': recipe.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['recipe'].pk, recipe.pk)
        self.assertEqual(resp.templates[0].name, 'recipe/recipe_print.html')

    def test_edit(self):
        recipe = Recipe.objects.get(pk=1)

        # sanitty check
        self.assertEqual(recipe.author.username, 'admin')
        self.assertEqual(recipe.servings, 8)
        self.assertEqual(recipe.ingredients.count(), 12)
        resp = self.app.get(reverse('recipe_edit', kwargs={'user': 'admin', 'pk': recipe.pk}),
                            user='admin')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.forms[1])
        form = resp.forms[1]
        form['servings'] = '10'
        form['ingredients-13-quantity'] = '1'
        form['ingredients-13-measurement'] = 'cup'
        form['ingredients-13-title'] = 'cheddar cheese'
        resp = form.submit().follow()
        self.assertEqual(resp.request.url,
                         'http://testserver' + resp.context['recipe'].get_absolute_url())

        # make sure the form saved our changes
        # got to get the recipe again so that it gets our new numbers after the save
        recipe = Recipe.objects.get(pk=1)
        self.assertEqual(recipe.servings, 10)
        self.assertEqual(recipe.ingredients.count(), 13)

        # test editing a non-existant recipe
        resp = self.app.get(reverse('recipe_edit', kwargs={'user': 'admin', 'pk': 123123}),
                            user='admin', status=404)
        self.assertEqual(resp.status_code, 404)

        # try having another user edit someone elses recipe
        resp = self.app.get(reverse('recipe_edit', kwargs={'user': 'admin', 'pk': recipe.pk}),
                            user='testUser', status=404)
        self.assertEqual(resp.status_code, 404)
