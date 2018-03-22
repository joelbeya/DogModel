from django import forms
from django.http import *
from django.contrib.auth.hashers import *
from .models import *
from datetime import datetime

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


def affiche(request):
    mail = request.POST['mail']
    password = make_password(request.POST['password'])
    nom = request.POST['name']
    prenom = request.POST['first_name']
    sexe = request.POST['sexe']
    date_naissance = request.POST['birth']

    User.objects.create(mail=mail, password=password, nom=nom, prenom=prenom, sexe=sexe, date_naissance=date_naissance)
    
    return HttpResponse("Vous avez été enregistré !")