from django.conf.urls import url
from . import views
from .models import *

app_name='dogo'

urlpatterns = [
	url(r'^index/$', views.index, name='index'),
	url(r'^formu/$', views.formu),
    url(r'^(?P<obj>[A-Za-z]*)/$', views.requete),
    url(r'^(?P<obj>[A-Za-z]*)/(?P<key>[0-9]*)/$', views.show),

]
