from django.db import models

# Create your models here.
class race(models.Model):
    """docstring for race."""
    taille = models.CharField(max_length = 255)
    nom_race = models.CharField(max_length = 255)
    morphologie = models.CharField(max_length = 255)
    traits_comportementaux = models.TextField(max_length = 255)

    def __init__(self, arg):
        super(race, self).__init__()
        self.arg = arg
