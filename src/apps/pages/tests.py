"""
https://docs.djangoproject.com/en/4.0/topics/testing/tools.html

Run the test as follows:
python manage.py test apps.gatepasses.tests
"""


from django.test import Client, TestCase


class PagesTestCase(TestCase):

    fixtures = [
        "pages.json",
    ]

    def setUp(self):

        # Every test needs a client.
        self.client = Client(HTTP_USER_AGENT="Mozilla/5.0")

    def test_about_page(self):

        # Issue a GET request.
        response = self.client.get("/about/")

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

