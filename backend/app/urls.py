from django.urls import path
from . import views  # Import views from the current app

app_name = 'backApp'
urlpatterns = [
    path('', views.home, name='home'),  # Maps the root URL to the home view    
    path('success/', views.success, name='success'),
    path('Admin/', views.Admin, name='Admin') , 
    path('authentification/', views.authentification, name='authentifications'),
    path('medecin/', views.medecin, name='medecin') , 
    path('infirmier/', views.Infirmier, name='infrimier') , 
    path('laborantin/', views.laborantin, name='laborantin') , 
    path('radiologue/', views.radiologue, name='radiologue') , 
    path('patient/', views.patient, name='patient') , 
    path('technicien/', views.technicien, name='technicien') , 
    path('error/', views.error, name='error') ,


]  

