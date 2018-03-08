from django.shortcuts import render
from .models import *
from .forms import *
import sys

# Create your views here.

def index(request):
    objets = Chien.objects.all();
    return render(request, 'dogo/index.html', {'objets':objets})

def requete(request,obj):
    identifier = getattr(sys.modules[__name__], obj)
    objets = identifier.all()
    return render(request, 'dogo/requete.html', {'objets':objets})

def show(request, obj, key):
    identifier = getattr(sys.modules[__name__], obj)
    objet = identifier.find(int(key))
    return render(request, 'dogo/show.html', {'objet':objet})

def formu(request):
    return render(request, 'dogo/formu.html', {'form':Subscribe})
