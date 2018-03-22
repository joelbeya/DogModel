from django.db import models
from django.conf import settings

class Race(models.Model):
    nom = models.CharField(max_length = 255)
    taille = models.IntegerField()
    morphologie = models.CharField(max_length = 255)
    traits_comportementaux = models.CharField(max_length = 255)

    @classmethod
    def all(self):
        return Race.objects.all()

    @classmethod
    def find(self, key):
        try:
            return Race.objects.filter(pk=key)
        except:
            raise Http404('Google who are you {} ?')

    def __str__(self):
        return self.nom




class Proprietaire(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, null=True)
    date_naissance= models.DateField()
    adresse = models.CharField(max_length=255)
    sexe = models.BooleanField()

    @classmethod
    def all(self):
        return Proprietaire.objects.all()

    @classmethod
    def find(self, key):
        try:
            return Proprietaire.objects.filter(pk=key)
        except:
            raise Http404('Google who are you {} ?')

    def __str__(self):
        return self.nom



class Chien(models.Model):
    nom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    couleur_poils = models.CharField(max_length=255)
    couleur_yeux = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1)
    proprio = models.ForeignKey(Proprietaire,on_delete=models.CASCADE)
    race = models.ForeignKey(Race,on_delete=models.CASCADE)
    pere = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='enfant_pere')
    mere = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='enfant_mere')
    
    @classmethod
    def all(self):
        return Chien.objects.all()

    @classmethod
    def find(self, key):
        try:
            return Chien.objects.filter(pk=key)
        except:
            raise Http404('Google who are you {} ?')

    def __str__(self):
        return self.nom



class User(models.Model):
    mail = models.CharField(max_length=255)
    password = models.CharField(max_length=500)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1)
    date_naissance = models.DateField()

    @classmethod
    def all(self):
        return User.objects.all()

    @classmethod
    def find(self, key):
        try:
            return User.objects.filter(pk=key)
        except:
            raise Http404('Google who are you {} ?')

    def __str__(self):
        return self.mail