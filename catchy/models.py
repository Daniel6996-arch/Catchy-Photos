from django.db import models

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
    image_name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(category)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']    
        