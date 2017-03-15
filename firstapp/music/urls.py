
from django.conf.urls import include, url
from . import views

app_name = 'music'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/model/id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
]
