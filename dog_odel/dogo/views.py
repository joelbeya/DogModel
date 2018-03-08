from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import sys

# Create your views here.

def index(request):
    return HttpResponse("Test")

def indexx(request,obj):
    identifier = getattr(sys.modules[__name__], obj)
    objets = identifier.all()
    return render(request, 'dogo/index.html', {'objets':objets})

def show(request, obj, key):
    objet = obj.find(key)
    return render(request, 'dogo/show.html', {'objet':objet})
