from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Maps the root URL to the home view    
    path('success/', views.success, name='success'),
    path('Admin/', views.Admin, name='Admin') , 
    path('authentification/', views.authentification, name='authentifications'),
    path('medecin/', views.medecin, name='medecin') , 
    path('infirmier/', views.infirmier, name='infirmier') , 
    path('laborantin/', views.laborantin, name='laborantin') , 
    path('radiologue/', views.radiologue, name='radiologue') , 
    path('error/', views.error, name='error') ,
    path('soin/', views.soinCreated, name='soin_created') ,


]  
