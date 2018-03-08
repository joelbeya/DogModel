#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

print("Cela va supprimer toute la base de données pour rajouter de nouvelles instance, en êtes-vous sûrs ?")
input("Appuyez sur uen touche pour valider")


DELETE FROM *

#Ajout des Proprios
Proprietaire.objects.create(nom="Baba",prenom="Bibi",date_naissance="2006-10-25",adresse="Mtp",sexe=True)

#Ajout des Races
Race.objects.create(nom="Berger",taille=120,morphologie="musclé",traits_comportementaux="agressif")

#Ajout des Chiens
Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(1),race=Race(1))
Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(1),race=Race(1))
Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(1),race=Race(1),pere=Chien(1),mere=Chien(2))