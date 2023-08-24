from django.test import TestCase
from django.urls import reverse

class PagesTest(TestCase):

    def test_home_page_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_show_home_page_title_in_home_page_view(self):
        response = self.client.get('')
        self.assertContains(response, 'Home Page')

    def test_aboutus_page_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_url_by_name(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)

    def test_show_aboutus_page_title_in_aboutus_page_view(self):
        response = self.client.get('/aboutus/')
        self.assertContains(response, 'About Us')    