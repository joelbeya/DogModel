from django.conf.urls import url
from . import views
from .models import *

app_name='dogo'

urlpatterns = [
	url(r'^index/$', views.index),
    url(r'^index/(?P<obj>[A-Za-z]*)/$', views.indexx),
    url(r'^index/(?P<obj>[A-Za-z]*)/(?P<key>[0-9]+)/$', views.show),
]
