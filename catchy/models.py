from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=120)
    def __str__(self):
        return self.location

class Category(models.Model):
    category =  models.CharField(max_length=30)
    def __str__(self):
        return self.category   

class Image(models.Model):
    image_name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()          