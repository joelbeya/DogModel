
from django.conf.urls import url
from . import views

app_name='dogo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dog/(?P<id>[0-9]+)$', views.show, name='show'),
]
