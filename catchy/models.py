from django.db import models
from PIL import Image
import PIL.Image as Image

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=120)
    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()         

class category(models.Model):
    category =  models.CharField(max_length=30)
    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']       

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', default='SOME STRING')
    image_name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(category)

    
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category=search_term)
        return photos

    @classmethod
    def gallery(cls):
        photos = cls.objects.all().order_by('location')           
        return photos