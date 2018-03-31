from django.shortcuts import render
from .models import *
from .forms import *
import sys
from django.contrib.auth import logout

# Create your views here.

def index(request):
    objets = Chien.objects.order_by('-created_at');
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

def formu_submit(request):
	return affiche(request)

def login(request):
	return render(request, 'dogo/login.html', {'form':Login})

def sub(request):
	return log(request)

def log_out(request):
    logout(request)
    return redirect(reverse(login))
