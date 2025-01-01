from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient")
    num_securite_sociale = models.CharField(max_length=50, unique=True)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=[("M", "Masculin"), ("F", "Feminin")], default="M")
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    medecin_traitant = models.CharField(max_length=100)
    personne_contact = models.CharField(max_length=100)
    medecin = models.ForeignKey('Medecin', on_delete=models.CASCADE, related_name="patients_set")
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - NSS: {self.num_securite_sociale}"


class Medecin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="medecin_set")
    patients = models.ManyToManyField(Patient, related_name="medecin")
    
    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"


class Pharmacien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pharmacien")

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"


class Infirmier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="infirmier")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Laborantin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="laborantin")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Radiologue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="radiologue")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Consultation(models.Model):
    motif = models.CharField(max_length=255)
    date = models.DateField()
    resume = models.TextField()
    dossier = models.ForeignKey('DossierPatient', on_delete=models.CASCADE, related_name="consultations")
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, related_name="consultations")

    def __str__(self):
        return f"Consultation on {self.date} - Motif: {self.motif}"


class Examen(models.Model):
    examen_id = models.AutoField(primary_key=True, serialize=True)
    type = models.CharField(max_length=50)
    date = models.DateField()
    resultat = models.TextField()

    class Meta:
        abstract = True


class ExamenRadiologique(Examen):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name="radiologiques")
    type_image = models.CharField(max_length=50)
    fichier_image = models.TextField()
    compte_rendu = models.TextField()
    radiologue = models.ForeignKey(Radiologue, on_delete=models.CASCADE, related_name="examens_radiologiques")


class ExamenBiologique(Examen):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name="biologiques")
    parametres = models.TextField()
    valeurs = models.TextField()
    graphique_tendance = models.TextField()
    laborantin = models.ForeignKey(Laborantin, on_delete=models.CASCADE, related_name="examens_biologiques")

class CompteRendu(models.Model):
    date = models.DateField()
    contenu = models.TextField()
    auteur = models.CharField(max_length=50)
    examen = models.ForeignKey(ExamenRadiologique, on_delete=models.CASCADE, related_name="compte_rendus", blank=True, null=True)
    

class Medicament(models.Model):
    nom = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    voie_administration = models.CharField(max_length=50)


class OrdonnanceMedicament(models.Model):
    ordonnance = models.ForeignKey('Ordonnance', on_delete=models.CASCADE, related_name="ordonnances_medicaments")
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name="ordonnances_medicaments")


class DossierPatient(models.Model):
    date_creation = models.DateField()
    num_securite_sociale = models.CharField(max_length=50, unique=True)


class Antecedent(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()
    date_declaration = models.DateField()
    dossier = models.ForeignKey(DossierPatient, on_delete=models.CASCADE, related_name="antecedents")


class CertificatMedical(models.Model):
    date_emission = models.DateField()
    motif = models.CharField(max_length=255)
    date_arret = models.CharField(max_length=50)
    dossier = models.ForeignKey(DossierPatient, on_delete=models.CASCADE, related_name="certificats_medicaux")


class Soin(models.Model):
    date = models.DateField()
    type = models.TextField()
    description = models.TextField()
    infirmier = models.ForeignKey(Infirmier, on_delete=models.CASCADE, related_name="soins")
    dossier = models.ForeignKey(DossierPatient, on_delete=models.CASCADE, related_name="soins")
    observation = models.TextField()


class Ordonnance(models.Model):
    date = models.DateField()
    duree = models.CharField(max_length=50)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name="ordonnances")



