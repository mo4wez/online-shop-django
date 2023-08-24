from django.test import TestCase
from django.urls import reverse

class AccountsTest(TestCase):

    def test_signup_page_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_show_signup_title_in_page(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'Sign Up')

    def test_signup_template_used(self):
        response = self.client.get('/accounts/signup/')
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_login_page_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_template_used(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'registration/login.html')
    
    def test_show_login_title_in_page(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Log In')

    