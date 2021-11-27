from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image
# Create your views here.
def home(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def gallery(request):
    photos = Image.gallery()
    return render(request, 'gallery.html', {"photos":photos})   

def photo(request):
    return render(request, 'photo.html') 

def search(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"photos":searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})                  
