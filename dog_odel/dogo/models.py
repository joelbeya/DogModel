from django.db import models
class Article(models.Model):
    nom = models.TextField(max_length=15)
    prenom = models.TextField(null=True, max_length=15)
    dateDeNaissance= models.DateTimeField(default=timezone.now,verbose_name="Date de Naissance")
    sexe = models.CharField(max_length=1)
    adresse = models.CharField(max_length=40)
# Create your models here.
