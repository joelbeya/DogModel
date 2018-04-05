from django.conf.urls import url
from . import views
from .models import *

app_name='dogo'

urlpatterns = [
	url(r'^$', views.index),
	url(r'^index$', views.index),
	url(r'^subscribe', views.formu_submit),
	url(r'^login', views.log),
	url(r'^logout', views.log_out),
    url(r'^(?P<obj>[A-Za-z]*)$', views.requete),
    url(r'^(?P<obj>[A-Za-z]*)/(?P<key>[0-9]*)$', views.show),
]
