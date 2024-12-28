from django.contrib import admin
from .models import *
admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Infirmier)
admin.site.register(Laborantin)
admin.site.register(Radiologue)
admin.site.register(Soin)
admin.site.register(Ordonnance)
admin.site.register(Consultation)
admin.site.register(DossierPatient)


# Register your models here.
