from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^gallery/$',views.gallery,name='gallery'),
    url('query/photo/(?P<image_id>\d+)/',views.photo,name='photo'),
    url('^search/',views.search,name='search')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
