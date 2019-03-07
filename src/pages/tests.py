from django.test import TestCase

# Create your tests here.
# tests.py is for our app-specific tests

class PagesTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_blog_page_status_code(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about-us/')
        self.assertEqual(response.status_code, 200)