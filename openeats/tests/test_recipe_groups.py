from django.contrib.auth.models import User
from django.test import TestCase

from openeats.models.recipe_groups import Course


class CourseTest(TestCase):
    """Test that course save overide works and course routing works"""
    fixtures = ['test_user_data.json', 'course_data.json']

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.assertEquals(self.user.username, 'testUser')

    def testCoursePage(self):
        """Test the course web page"""
        from django.core.urlresolvers import reverse
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'openeats/recipe_groups/course_list.html')
        courses = response.context['object_list']
        self.assertEqual(len(courses), 6,
                         'There should be 5 courses on the page but we found %s' % len(courses))

