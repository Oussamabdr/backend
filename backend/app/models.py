from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient", default=6)
    nss = models.BigIntegerField(primary_key=True, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=200)
    num_telephone = models.BigIntegerField(unique=True, default="Unknown")
    mutuelle = models.IntegerField(default="Unknown")
    medecin_trataint = models.CharField(max_length=100, default="Unknown")
    num_personne_a_contacter = models.BigIntegerField(default="Unknown")
    sexe = models.CharField(max_length=1, choices=[("M", "Masculin"), ("F", "Feminin")], default="M")

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Medecin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="medecin", null=False, default=1)
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def rechercher_consultations(self, nss: str):
        pass

    def editer_ordonance(self, prescription):
        pass

    def prescrire_examen(self, examen):
        pass

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Infermier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="infermier", default=2)
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def saisir_observations(self, nss: str):
        pass

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Laborantin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="laborantin", default=3)
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Radiologue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="radiologue", default=4)
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def uploader_image_medicale(self):
        pass

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Technicien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="technicien", default=5)
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def analyser_resultats_examen(self, examen):
        pass

    def __str__(self):
        return f"{self.nom} {self.prenom}"

