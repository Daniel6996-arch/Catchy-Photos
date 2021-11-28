from django.test import TestCase
from .models import Location, category, Image

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new location
        self.new_location= Location(location ='Nairobi')
        self.new_location.save_location()


        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))
        new_location = Image.location
        self.assertTrue(len(new_location) == 0) 

