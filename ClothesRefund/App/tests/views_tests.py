#This file contains the tests for the views. I have tested the views for the index page, the clothes list page, the add clothes page, the remove clothes page, and the edit clothes page. I have also tested the negative tests for the views. I haven't make any tests for all the pages who aren't in the url file, such as all the signup, password forget or password reset pages.
from django.test import TestCase
from django.urls import reverse
from App.models import Clothes  
from django.contrib.auth.models import User
class ViewsTests(TestCase):
    def test_views(self):
        # Test the index page
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'App/index.html')
        # Test the clothes list page
        response = self.client.get(reverse('clothes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'App/clothes_list.html')
        # Test the add clothes page
        response = self.client.get(reverse('addclothes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'App/addclothes.html')
        # Test the remove clothes page
        response = self.client.get(reverse('remove_clothes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'App/remove_clothes.html')
        # Test the edit clothes page
        response = self.client.get(reverse('edit_clothes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'App/edit_clothes.html')

    #negatives tests for the views
    def test_views_negative(self):
        # Test the index page
        response = self.client.get(reverse('index'))
        self.assertNotEqual(response.status_code, 404)
    def test_views_negative_2(self):
        # Test the clothes list page
        response = self.client.get(reverse('clothes_list'))
        self.assertNotEqual(response.status_code, 404)

