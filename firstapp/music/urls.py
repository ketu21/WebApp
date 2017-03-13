
from django.conf.urls import include, url
from . import views

app_name = 'music'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #/model/id/
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),
    #/model/id/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name= 'favorite')

]
