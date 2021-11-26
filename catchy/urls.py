from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^home/',views.index,name='index'),
    url('^gallery/',views.gallery,name='gallery'),
    url('^photo/',views.photo,name='photo'),
    url('^search/',views.search_results,name='search')
]