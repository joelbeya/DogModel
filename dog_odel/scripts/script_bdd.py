from django.db import models
from .models import Proprietaire,Race,Chien

print("Cela va supprimer toute la base de données pour rajouter de nouvelles instances, en êtes-vous sûrs ?")
input("Appuyez sur une Entrée pour valider")


Proprietaire.objects.all().delete()
Race.objects.all().delete()
Chien.objects.all().delete()

#Ajout des Proprios
Proprietaire.objects.create(nom="Stanton",prenom="Lani",date_naissance="1943-07-12",adresse="CP 261, 496 Mus. Route",sexe=1)
Proprietaire.objects.create(nom="Dickerson",prenom="Kristen",date_naissance="1993-07-06",adresse="CP 303, 9196 Orci Ave",sexe=1)
Proprietaire.objects.create(nom="Holmes",prenom="Lara",date_naissance="1938-05-15",adresse="1503 Vel, Avenue",sexe=1)
Proprietaire.objects.create(nom="Duran",prenom="Amaya",date_naissance="1991-04-26",adresse="9193 Eros Ave",sexe=0)
Proprietaire.objects.create(nom="Palmer",prenom="Cheyenne",date_naissance="1993-11-24",adresse="CP 283, 8229 Curae Route",sexe=0)
Proprietaire.objects.create(nom="Koch",prenom="Isaiah",date_naissance="1987-06-05",adresse="Appartement 712-2889 Amet, Av.",sexe=1)
Proprietaire.objects.create(nom="Anthony",prenom="Candace",date_naissance="1954-12-23",adresse="Appartement 828-4215 Ut Ave",sexe=0)
Proprietaire.objects.create(nom="Welch",prenom="Omar",date_naissance="1955-02-22",adresse="CP 461, 2672 Magna Avenue",sexe=1)
Proprietaire.objects.create(nom="West",prenom="Louis",date_naissance="1955-11-20",adresse="8519 Donec Ave",sexe=1)
Proprietaire.objects.create(nom="Haney",prenom="Aspen",date_naissance="1984-10-04",adresse="141-8057 Ac Av.",sexe=0)
Proprietaire.objects.create(nom="Whitney",prenom="Tiger",date_naissance="1946-04-21",adresse="578-3953 Phasellus Av.",sexe=0)
Proprietaire.objects.create(nom="Hines",prenom="Heather",date_naissance="1932-07-18",adresse="Appartement 156-6803 Ad Route",sexe=1)
Proprietaire.objects.create(nom="Doyle",prenom="Raya",date_naissance="1938-01-29",adresse="786-8278 Urna. Av.",sexe=1)
Proprietaire.objects.create(nom="Leon",prenom="Molly",date_naissance="1953-09-11",adresse="4004 Enim. Rd.",sexe=0)
Proprietaire.objects.create(nom="Graham",prenom="Kaseem",date_naissance="1963-06-11",adresse="922-5445 At Rd.",sexe=0)
Proprietaire.objects.create(nom="Church",prenom="Basil",date_naissance="1955-06-04",adresse="CP 598, 4452 Libero Ave",sexe=1)
Proprietaire.objects.create(nom="Mayer",prenom="Debra",date_naissance="1995-03-13",adresse="9109 Rhoncus. Avenue",sexe=0)
Proprietaire.objects.create(nom="Cardenas",prenom="Brendan",date_naissance="1988-10-20",adresse="526-4293 Cursus Rue",sexe=1)
Proprietaire.objects.create(nom="Foster",prenom="Keefe",date_naissance="1953-04-20",adresse="4234 Non, Ave",sexe=0)
Proprietaire.objects.create(nom="Gray",prenom="Cynthia",date_naissance="1935-03-13",adresse="754-3237 Integer Chemin",sexe=0)
Proprietaire.objects.create(nom="Aguilar",prenom="Sopoline",date_naissance="1984-03-12",adresse="3979 Lobortis Rue",sexe=0)
Proprietaire.objects.create(nom="Ramirez",prenom="Adena",date_naissance="1943-07-25",adresse="602-1116 Risus Chemin",sexe=0)
Proprietaire.objects.create(nom="Hubbard",prenom="Nicholas",date_naissance="1943-09-24",adresse="CP 237, 8361 Odio Av.",sexe=0)

#Ajout des Races
Race.objects.create(nom="Justice",taille=119,morphologie="felis",traits_comportementaux="eu")
Race.objects.create(nom="Good",taille=43,morphologie="rum",traits_comportementaux="nunc")
Race.objects.create(nom="Harper",taille=143,morphologie="dolor",traits_comportementaux="metus")
Race.objects.create(nom="Lynch",taille=120,morphologie="mon",traits_comportementaux="velit")
Race.objects.create(nom="Frost",taille=151,morphologie="ligula",traits_comportementaux="Suspendisse")
Race.objects.create(nom="Thompson",taille=126,morphologie="Duis",traits_comportementaux="ipsum")
Race.objects.create(nom="Buchanan",taille=158,morphologie="Donec",traits_comportementaux="commodo")
Race.objects.create(nom="Garcia",taille=20,morphologie="Donec",traits_comportementaux="Suspendisse")
Race.objects.create(nom="Herrera",taille=149,morphologie="natoque",traits_comportementaux="Donec")
Race.objects.create(nom="Berger",taille=120,morphologie="musclé",traits_comportementaux="agressif")

#Ajout des Chiens
Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(1),race=Race(1))
Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(1),race=Race(2))
Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(2),race=Race(4),pere=Chien(1),mere=Chien(2))
Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="rouge",sexe="M",proprio=Proprietaire(3),race=Race(8))
Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(9),race=Race(9))
Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(3),race=Race(10),pere=Chien(4),mere=Chien(5))
Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="bleu",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(12),race=Race(7))
Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(14),race=Race(1))
Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(5),race=Race(2),pere=Chien(1),mere=Chien(2))
Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(6),race=Race(5))
Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="marron",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(7),race=Race(6))
Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(8),race=Race(7),pere=Chien(1),mere=Chien(2))
Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(10),race=Race(7))
Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(11),race=Race(7))
Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(12),race=Race(9),pere=Chien(10),mere=Chien(8))
Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(15),race=Race(1))
Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(17),race=Race(3))
Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(18),race=Race(4),pere=Chien(10),mere=Chien(8))
