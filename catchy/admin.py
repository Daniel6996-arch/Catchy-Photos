from django.contrib import admin
from .models import Location, category, Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Location)
admin.site.register(category)
admin.site.register(Image, ImageAdmin)
