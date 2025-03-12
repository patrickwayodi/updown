"""
Run the test as follows:
python manage.py test apps.uploads.tests
"""


from django.test import Client, TestCase


class UploadDetailTestCase(TestCase):

    """
    https://docs.djangoproject.com/en/4.2/topics/testing/tools.html
    """

    fixtures = [
        "uploads.json",
    ]

    def setUp(self):

        # Every test needs a client.
        self.client = Client(HTTP_USER_AGENT="Mozilla/5.0")

    def test_upload_detail(self):

        # Issue a GET request.
        response = self.client.get("/upload/1/")

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

