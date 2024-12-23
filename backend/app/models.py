from django.db import models

class Patient(models.Model):
    num_securite_sociale = models.CharField(max_length=50)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField() 
    adress = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)  
    password = models.CharField(max_length=255)
    medecin_traitant = models.CharField(max_length=100)
    personne_contact = models.CharField(max_length=100)

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=255)

class Infirmier(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=255)

class Laborantin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=255)
    
class Radiologue(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=255)
    


# Create your models here.
from django.db import models

class Patient(models.Model):
    num_securite_sociale = models.CharField(max_length=50)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField() 
    adress = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)  
    password = models.CharField(max_length=255)
    medecin_traitant = models.CharField(max_length=100)
    personne_contact = models.CharField(max_length=100)

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=255)

class Infirmier(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=255)

class Laborantin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=255)
    
class Radiologue(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=255)
    


# Create your models here.
