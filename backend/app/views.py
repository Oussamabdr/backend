from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *

def Admin(request):
    if request.method == "POST" and request.POST.get('role') == 'patient':
        num_securite_sociale = request.POST.get('num_securite_sociale')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_naissance = request.POST.get('date_naissance')
        adress = request.POST.get('adress')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        medecin_traitant = request.POST.get('medecin_traitant')
        personne_contact = request.POST.get('personne_contact')

        # Create a new Patient instance
        Patient.objects.create(
            num_securite_sociale=num_securite_sociale,
            nom=nom,
            prenom=prenom,
            date_naissance=date_naissance,
            adress=adress,
            telephone=telephone,
            email=email,
            password=password,
            medecin_traitant=medecin_traitant,
            personne_contact=personne_contact
        )

        # Redirect or display a success message
        return redirect('success')  # Replace 'success' with your URL name or template

    if request.method == "POST" and request.POST.get('role') == 'medecin':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new Medecin instance
        Medecin.objects.create(
            nom=nom,
            prenom=prenom,
            email=email,
            password=password,
        )

        # Redirect or display a success message
        return redirect('medecin')  # Replace 'medecin' with your URL name or template
    if request.method == "POST" and request.POST.get('role') == 'infirmier':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new Medecin instance
        Infirmier.objects.create(
            nom=nom,
            prenom=prenom,
            email=email,
            password=password,
        )

        # Redirect or display a success message
        return redirect('infirmier')  # Replace 'medecin' with your URL name or template
    if request.method == "POST" and request.POST.get('role') == 'laborantin':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new Medecin instance
        Laborantin.objects.create(
            nom=nom,
            prenom=prenom,
            email=email,
            password=password,
        )
        return redirect('laborantin')
    if request.method == "POST" and request.POST.get('role') == 'radiologue':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new Medecin instance
        Radiologue.objects.create(
            nom=nom,
            prenom=prenom,
            email=email,
            password=password,
        )

        # Redirect or display a success message
        return redirect('radiologue')  # Replace 'medecin' with your URL name or template

    
    return render(request,'admin.html')


def home(request):
 return render(request,'home.html')
def success(request):
 return render(request, 'create_patient.html')
def patient(request):
 return render(request,"patient.html")
def medecin(request):
 return render(request,"medecin.html")
def Infirmier(request):
 return render(request,"infirmier.html")
def laborantin(request):
 return render(request,"laborantin.html")
def radiologue(request):
 return render(request,"radiologue.html")
def technicien(request):
 return render(request,"technicien.html")
def error(request):
 return render(request,"error404.html")





def authentification(request):

    if request.method == "POST":
        role = request.POST.get('role')
        username = request.POST.get("username")
        password = request.POST.get("password")

        if role == 'admin' and username == "fatima" and password == "123":
            return redirect('Admin') 
        elif role == 'patient':
         try:
           user = Patient.objects.get(email=username) 
           if user.email == username and user.password == password :
              return redirect('success')
         except Patient.DoesNotExist:
              return redirect('error')
        elif role == 'medecin':
         try:
           user = Medecin.objects.get(email=username) 
           if user.email == username and user.password == password :
              return redirect('medecin')
         except Medecin.DoesNotExist:
              return redirect('error')
        elif role == 'infirmier':
         try:
           user = Infirmier.objects.get(email=username) 
           if user.email == username and user.password == password :
              return redirect('infirmier')
         except Infirmier.DoesNotExist:
              return redirect('error')
        elif role == 'laborantin':
         try:
           user = Laborantin.objects.get(email=username) 
           if user.email == username and user.password == password :
              return redirect('laborantin')
         except Laborantin.DoesNotExist:
              return redirect('error')
        elif role == 'radiologue':
         try:
           user = Radiologue.objects.get(email=username) 
           if user.email == username and user.password == password :
              return redirect('radiologue')
         except Radiologue.DoesNotExist:
              return redirect('error')
        elif role == 'technicien':
         try:
            user = technicien.objects.get(email=username) 
            if user.email == username and user.password == password :
              return redirect('technicien')
         except Radiologue.DoesNotExist:
              return redirect('error')

    return render(request, "authentification.html")

# Create your views here.

