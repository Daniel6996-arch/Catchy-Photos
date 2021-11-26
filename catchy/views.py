from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')   

def photo(request):
    return render(request, 'photo.html')               
