# This file tests the urls for the app. I have tested the urls for the index page, the clothes list page, the add clothes page, the remove clothes page, and the edit clothes page. I have also tested the negative tests for the urls. I haven't make any tests for all the pages who aren't in the url file, such as all the signup, password forget or password reset pages.
from django.test import TestCase
from django.db import models
from App.models import Clothes
from django.urls import reverse, resolve
from App.views import index
from App.views import clothes_list
from App.views import addclothes
from App.views import remove_clothes
from App.views import edit_clothes
from App.views import SignUpView
class UrlTests(TestCase):
    # Test the url for the index page
    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    # Test the url for the clothes list page
    def test_clothes_url(self):
        url = reverse('clothes_list')
        self.assertEquals(resolve(url).func, clothes_list)
    
    # Test the url for the add clothes page
    def test_addclothes_url(self):
        url = reverse('addclothes')
        self.assertEquals(resolve(url).func, addclothes)
    
    # Test the url for the remove clothes page
    def test_remove_clothes_url(self):
        url = reverse('remove_clothes')
        self.assertEquals(resolve(url).func, remove_clothes)

    # Test the url for the edit clothes page
    def test_edit_clothes_url(self):
        url = reverse('edit_clothes')
        self.assertEquals(resolve(url).func, edit_clothes)
    
    #negative test for the url for the index page
    def test_index_url_negative(self):
        url = reverse('index')
        self.assertNotEquals(resolve(url).func, clothes_list)


    


    
