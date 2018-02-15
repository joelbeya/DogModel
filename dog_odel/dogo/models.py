from django.db import models

class Proprietaire(models.Model):
    nom = models.TextField(max_length=15)
    prenom = models.TextField(null=True, max_length=15)
    dateDeNaissance= models.DateTimeField(default=timezone.now,verbose_name="Date de Naissance")
    sexe = models.CharField(max_length=1)
    adresse = models.CharField(max_length=40)

class Race(models.Model):
    taille = models.CharField(max_length = 255)
    nom_race = models.CharField(max_length = 255)
    morphologie = models.CharField(max_length = 255)
    traits_comportementaux = models.TextField(max_length = 255)

    def __init__(self, arg):
        super(race, self).__init__()
        self.arg = arg

class Chien(models.Model):
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    couleur_poils = models.CharField(max_length=50)
    couleur_yeux = models.CharField(max_length=50)
    sexe = models.BooleanField()
    #descendant = models.ForeignKey(Chien,)
    proprio = models.ForeignKey(Proprietaire,on_delete=models.CASCADE)
    race = models.ForeignKey(Race,on_delete=models.CASCADE)