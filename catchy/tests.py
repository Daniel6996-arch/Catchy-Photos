from django.test import TestCase
from .models import Location, category, Image

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new image and saving it
        self.nairobi= Location(location ='Nairobi')


        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

