from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    num_securite_sociale = models.CharField(max_length=50)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adress = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    medecin_traitant = models.CharField(max_length=100)
    personne_contact = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom} - NSS: {self.num_securite_sociale}"


class Medecin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"Dr. {self.nom} {self.prenom}"

class Pharmacien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"Dr. {self.nom} {self.prenom}"


class Infirmier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Laborantin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Radiologue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Consultation(models.Model):
    motif = models.CharField(max_length=255)
    date = models.DateField()
    resume = models.TextField()
    dossier_id = models.ForeignKey('DossierPatient', on_delete=models.CASCADE)
    medecin_id = models.ForeignKey(Medecin, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consultation on {self.date} - Motif: {self.motif}"
    
class Examen(models.Model):
    type = models.CharField(max_length=50)
    date = models.DateField()
    resultat = models.TextField()
    consultation_id = models.ForeignKey('Consultation', on_delete=models.CASCADE)

class ExamenRadiologique(models.Model):
    type_image = models.CharField(max_length=50)
    fichier_image = models.TextField()
    compte_rendu = models.TextField()
    examen_id = models.ForeignKey('Examen', on_delete=models.CASCADE)
    radiologue_id = models.ForeignKey('Radiologue', on_delete=models.CASCADE)

class CompteRendu(models.Model):
    date = models.DateField()
    contenu = models.TextField()
    auteur_id = models.CharField(max_length=50)  
    examen_id = models.ForeignKey('Examen', on_delete=models.CASCADE)

class ExamenBiologique(models.Model):
    parametres = models.TextField()
    valeurs = models.TextField()
    graphique_tendance = models.TextField()
    examen_id = models.ForeignKey('Examen', on_delete=models.CASCADE)
    laborantin_id = models.ForeignKey('Laborantin', on_delete=models.CASCADE)

class Medicament(models.Model):
     nom = models.CharField(max_length=100)
     dosage = models.CharField(max_length=50)  
     voie_administration = models.CharField(max_length=50)

class OrdonnanceMedicament(models.Model):
     ordonnance_id = models.ForeignKey('Ordonnance', on_delete=models.CASCADE)
     medicament_id = models.ForeignKey('Medicament', on_delete=models.CASCADE)

class DossierPatient(models.Model):
    date_creation = models.DateField()
    num_securite_sociale = models.CharField(max_length=50)

class Antecedent(models.Model):
    type = models.CharField(max_length=100)  
    description = models.TextField()
    date_declaration = models.DateField()
    dossier_id = models.ForeignKey('DossierPatient', on_delete=models.CASCADE)

class CertificatMedical(models.Model):
    date_emission = models.DateField()
    motif = models.CharField(max_length=255)
    date_arret = models.CharField(max_length=50)
    dossier_id = models.ForeignKey('DossierPatient', on_delete=models.CASCADE)

class Soin(models.Model):
    date = models.DateField()
    type = models.TextField()  
    description = models.TextField()
    infirmier_id = models.ForeignKey('Infirmier', on_delete=models.CASCADE)  
    dossier_id = models.ForeignKey('DossierPatient', on_delete=models.CASCADE)  
    observation = models.TextField() 

class Ordonnance(models.Model):
    date = models.DateField()
    duree = models.CharField(max_length=50)
    consultation_id = models.ForeignKey('Consultation', on_delete=models.CASCADE)




# Create your models here.
