from __future__ import absolute_import

from django.test import TestCase
from django.db import IntegrityError
from .models import Course, Cuisine
from django.contrib.auth.models import User

class CourseTest(TestCase):
    """Test that course save overide works and course routing works"""
    fixtures = ['test_user_data.json','course_data.json'] #load a user up and course data

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.assertEquals(self.user.username, 'testUser') #make sure the user works
        
    def testSlugAutoset(self):
        """Verify the slug is auto set when a slug is not provided"""
        course = Course.objects.create(title='New Course', author=self.user)
        self.assertEqual(course.slug, 'new-course')


    def testCoursePage(self):
        """Test the course web page"""
        from django.core.urlresolvers import reverse
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200) #got the the page
        self.assertTemplateUsed(response, 'recipe_groups/course_list.html') #check the right template was used
        courses = response.context['object_list']
        self.assertEqual(len(courses), 6, 'There should be 5 courses on the page but we found %s' % len(courses))

    def tearDown(self):
        Course.objects.all().delete()
