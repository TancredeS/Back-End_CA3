#This file contains the tests for the Clothes model. I have tested the creation of a clothe, the deletion of a clothe, the modification of a clothe, and the negative tests for the clothes model.
#I haven't made any other tests for the clothes model, because I don't think it's necessary to test the clothes model, because it's just a model, and it doesn't have any functions.
from django.test import TestCase
from App.models import Clothes

class ClothesTests(TestCase):
    #test if the creation of a clothe is successful
    def test_clothes(self):
        clothes = Clothes(ClothesName='Shirt', ClothesMaterial='Cotton', ClothesSize='Large', ClothesBrand='Nike', ClothesColor='Red')
        self.assertEqual(clothes.ClothesName, 'Shirt')
        self.assertEqual(clothes.ClothesMaterial, 'Cotton')
        self.assertEqual(clothes.ClothesSize, 'Large')
        self.assertEqual(clothes.ClothesBrand, 'Nike')
        self.assertEqual(clothes.ClothesColor, 'Red')
    
    #test if the clothe is not empty
    def test_clothes_not_empty(self):
        clothes = Clothes(ClothesName='Shirt', ClothesMaterial='Cotton', ClothesSize='Large', ClothesBrand='Nike', ClothesColor='Red')
        self.assertNotEqual(clothes.ClothesName, '')
        self.assertNotEqual(clothes.ClothesMaterial, '')
        self.assertNotEqual(clothes.ClothesSize, '')
        self.assertNotEqual(clothes.ClothesBrand, '')
        self.assertNotEqual(clothes.ClothesColor, '')
    
    #test if at least one characteristic of the clothe is empty
    def test_clothes_at_least_one_empty(self):
        clothes = Clothes(ClothesName='Shirt', ClothesMaterial='Cotton', ClothesSize='Large', ClothesBrand='', ClothesColor='Red')
        if clothes.ClothesName == '' or clothes.ClothesMaterial == '' or clothes.ClothesSize == '' or clothes.ClothesBrand == '' or clothes.ClothesColor == '':
            self.assertTrue(True)
        else:
            self.assertTrue(False)
    
    #test if the all the characteristics of the clothe are strings
    def test_clothes_all_strings(self):
        clothes = Clothes(ClothesName='Shirt', ClothesMaterial='Cotton', ClothesSize='Large', ClothesBrand='Nike', ClothesColor='Red')
        self.assertTrue(isinstance(clothes.ClothesName, str))
        self.assertTrue(isinstance(clothes.ClothesMaterial, str))
        self.assertTrue(isinstance(clothes.ClothesSize, str))
        self.assertTrue(isinstance(clothes.ClothesBrand, str))
        self.assertTrue(isinstance(clothes.ClothesColor, str))

    #test if after the deletion of a clothe the clothe is not in the database
    def test_clothes_delete(self):
        clothes = Clothes(ClothesName='Shirt', ClothesMaterial='Cotton', ClothesSize='Large', ClothesBrand='Nike', ClothesColor='Red')
        clothes.save()
        clothes.delete()
        self.assertFalse(Clothes.objects.filter(ClothesName='Shirt').exists())
    
    #negative test for the creation of a clothe
    def test_clothes_negative(self):
        clothes = Clothes(ClothesName='Shirt', ClothesMaterial='Cotton', ClothesSize='Large', ClothesBrand='Nike', ClothesColor='Red')
        self.assertEqual(clothes.ClothesName, 'Pants')
        self.assertEqual(clothes.ClothesMaterial, 'Leather')
        self.assertEqual(clothes.ClothesSize, 'Small')
        self.assertEqual(clothes.ClothesBrand, 'Adidas')
        self.assertEqual(clothes.ClothesColor, 'Blue')
    
    #negative test after edition of the clothe
    def test_clothes_negative_after_edit(self):
        clothes = Clothes(ClothesName='Shirt', ClothesMaterial='Cotton', ClothesSize='Large', ClothesBrand='Nike', ClothesColor='Red')
        clothes.save()
        clothes.ClothesName = 'Pants'
        clothes.ClothesMaterial = 'Leather'
        clothes.ClothesSize = 'Small'
        clothes.ClothesBrand = 'Adidas'
        clothes.ClothesColor = 'Blue'
        clothes.save()
        self.assertEqual(clothes.ClothesName, 'Shirt')
        self.assertEqual(clothes.ClothesMaterial, 'Cotton')
        self.assertEqual(clothes.ClothesSize, 'Large')
        self.assertEqual(clothes.ClothesBrand, 'Nike')
        self.assertEqual(clothes.ClothesColor, 'Red')
    



