from django.db import models
from django.conf import settings

# Create your models here.

class Race(models.Model):
    taille = models.CharField(max_length = 255)
    nom_race = models.CharField(max_length = 255)
    morphologie = models.CharField(max_length = 255)
    traits_comportementaux = models.TextField(max_length = 255)

class Proprietaire(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(null=True, max_length=255)
    dateDeNaissance= models.DateField()
    adresse = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1)


class Chien(models.Model):
    nom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    couleur_poils = models.CharField(max_length=255)
    couleur_yeux = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1)
    proprio = models.ForeignKey(Proprietaire,on_delete=models.CASCADE)
    race = models.ForeignKey(Race,on_delete=models.CASCADE)
