from django import forms
from django.http import *
from django.contrib.auth.hashers import *
from .models import *
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

class Subscribe(forms.Form):
    mail = forms.EmailField(label='Your e-mail', max_length=100)
    name = forms.CharField(label='Your name', max_length=100)
    first_name = forms.CharField(label='Your first name', max_length=100)
    choix = (
        ('Male', 'M'),
        ('Femelle', 'F'),
    )
    sexe = forms.ChoiceField(label='Your civility', choices=choix)
    birth = forms.DateField()
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
            'password': forms.PasswordInput(),
        }

class Login(forms.Form):
    mail = forms.EmailField(label='Your e-mail', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
            'password': forms.PasswordInput(),
        }


def affiche(request):
    mail = request.POST['mail']
    password = make_password(request.POST['password'])
    nom = request.POST['name']
    prenom = request.POST['first_name']
    sexe = request.POST['sexe']
    date_naissance = request.POST['birth']

    User.objects.create(mail=mail, password=password, nom=nom, prenom=prenom, sexe=sexe, date_naissance=date_naissance)
    
    return HttpResponse("Vous avez été enregistré !")


def log(request):
    try:
        m = User.objects.get(mail=request.POST['mail'])
    except ObjectDoesNotExist:
        return HttpResponse("Your username and password didn't match.")

    if check_password(request.POST['password'], m.password):
        request.session['id'] = m.id
        return redirect('/dogo/index')
    else:
        return HttpResponse("Your username and password didn't match.")


def logout(request):
    try:
        logout(request)
    except KeyError:
        pass
    return redirect('/dogo/index')