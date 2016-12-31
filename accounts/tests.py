from django_webtest import WebTest
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class accountViewsTestCase(WebTest):
    fixtures = ['test_user_data.json']
    setup_auth = False

    def test_admin_login(self):
        # sanity check to make sure the data loaded
        user = User.objects.get(username="admin")
        self.assertEqual(user.is_staff, True)
        self.assertTrue(user.is_active)
        self.assertEqual(user.username, 'admin')
        self.assertTrue(user.check_password('password'))

        # login to the form
        url = reverse('auth_login')
        form = self.app.get(url).forms[1]
        form['username'] = 'admin'
        form['password'] = 'password'
        resp = form.submit()
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, reverse('recipe_index'))

    def test_login(self):
        """used to test the login form"""

        #sanity check to make sure the data loaded
        user = User.objects.get(username="testUser")
        self.assertEqual(user.username, 'testUser')
        self.assertTrue(user.check_password('password'))

        #login to the form
        form = self.app.get(reverse('auth_login')).forms[1]
        form['username'] = 'testUser'
        form['password'] = 'password'
        resp = form.submit()
        self.assertEqual(resp.location, 'http://localhost:80' + reverse('recipe_index'))
        self.assertEqual(resp.status_code, 302)

    def test_bad_login(self):
        """make sure an error is thrown when someone can't login"""
        form = self.app.get(reverse('auth_login')).forms[1]
        form['username'] = 'testUser'
        form['password'] = 'baspassword'
        resp = form.submit()
        self.assertEqual(resp.status_code, 200)

    def test_create_user(self):
        """test that a user can be created"""
        form = self.app.get(reverse('registration_register')).forms[1]
        form['username'] = 'newUser'
        form['email'] = 'newUser@yahoo.com'
        form['password1'] = 'password'
        form['password2'] = 'password'
        resp = form.submit().follow()
        self.assertTrue('Thank you' in resp.body)

        #check the signal on save of a new user created a profile for the user
        profile = self.app.get(reverse('profiles_profile_detail', kwargs={'username':'newUser'}))
        self.assertTrue(profile.status_code, 200)

        #check a unknown user throws a 404 on the profile page
        profile = self.app.get(reverse('profiles_profile_detail', kwargs={'username':'badUser'}),status=404)
        self.assertTrue(profile.status_code, 404)

        

