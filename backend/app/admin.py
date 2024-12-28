from django.contrib import admin
from .models import *
admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Infirmier)
admin.site.register(Laborantin)
admin.site.register(Radiologue)
admin.site.register(Pharmacien)

# Register your models here.
