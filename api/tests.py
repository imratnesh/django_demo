# api/tests.py
from django.test import TestCase
from .utils import get_hello_world

from django.urls import reverse


class UtilsTests(TestCase):
    def test_get_hello_world(self):
        # Test the get_hello_world function
        result = get_hello_world()
        self.assertEqual(result, "HelloWorld")


class HelloWorldAPITests(TestCase):
    def test_hello_world_api(self):
        # Send a GET request to the API
        response = self.client.get(reverse('hello_world'))

        # Check the status code
        self.assertEqual(response.status_code, 200)

        # Check the response content
        expected_data = {'data': 'HelloWorld', 'status': True}
        self.assertJSONEqual(response.content, expected_data)

# python manage.py test api
# python manage.py test api.tests.UtilsTests.test_get_hello_world
