from .models import Clothes
from django.test import TestCase

class ClothesTests(TestCase):
    def test_clothes_name(self):
        clothes = Clothes(ClothesName='Shirt')
        self.assertEqual(clothes.ClothesName, 'Shirt')