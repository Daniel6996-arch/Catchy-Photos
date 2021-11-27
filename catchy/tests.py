from django.test import TestCase
from .models import Location, category, Image

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new location
        self.nairobi= Location(location ='Nairobi')
        self.nairobi.save_location()


        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
        self.assertTrue(len(nairobi) == 0) 

