from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^photo/',views.photo,name='photo'),
    url(r'search/',views.search_results,name='search')
]