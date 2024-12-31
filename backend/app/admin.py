from django.contrib import admin
from .models import *
admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Pharmacien)
admin.site.register(Infirmier)
admin.site.register(Laborantin)
admin.site.register(Radiologue)

admin.site.register(Consultation)
admin.site.register(Examen)
admin.site.register(ExamenRadiologique)
admin.site.register(CompteRendu)
admin.site.register(ExamenBiologique)

admin.site.register(Medicament)
admin.site.register(OrdonnanceMedicament)
admin.site.register(DossierPatient)
admin.site.register(Antecedent)
admin.site.register(CertificatMedical)

admin.site.register(Soin)
admin.site.register(Ordonnance)


# Register your models here.
