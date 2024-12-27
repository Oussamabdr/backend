from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def Admin(request):
    if request.method == "POST":
        role = request.POST.get('role')
        
        # Creating instances for each role
        if role == 'patient':
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
            user = User.objects.create_user(username=email, password=password, email=email)  # Create User instance
            Patient.objects.create(
                user=user,
                num_securite_sociale=num_securite_sociale,
                nom=nom,
                prenom=prenom,
                date_naissance=date_naissance,
                adress=adress,
                telephone=telephone,
                medecin_traitant=medecin_traitant,
                personne_contact=personne_contact
            )
            return redirect('success')  # Replace 'success' with your URL name or template

        elif role == 'medecin':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Create a new Medecin instance
            user = User.objects.create_user(username=email, password=password, email=email)  # Create User instance
            Medecin.objects.create(
                user=user,
                nom=nom,
                prenom=prenom,
                email=email,
            )
            return redirect('medecin')  # Replace 'medecin' with your URL name or template

        elif role == 'infirmier':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Create a new Infirmier instance
            user = User.objects.create_user(username=email, password=password, email=email)  # Create User instance
            Infirmier.objects.create(
                user=user,
                nom=nom,
                prenom=prenom,
                email=email,
            )
            return redirect('infirmier')  # Replace 'infirmier' with your URL name or template

        elif role == 'laborantin':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Create a new Laborantin instance
            user = User.objects.create_user(username=email, password=password, email=email)  # Create User instance
            Laborantin.objects.create(
                user=user,
                nom=nom,
                prenom=prenom,
                email=email,
            )
            return redirect('laborantin')  # Replace 'laborantin' with your URL name or template

        elif role == 'radiologue':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Create a new Radiologue instance
            user = User.objects.create_user(username=email, password=password, email=email)  # Create User instance
            Radiologue.objects.create(
                user=user,
                nom=nom,
                prenom=prenom,
                email=email,
            )
            return redirect('radiologue')  # Replace 'radiologue' with your URL name or template

    return render(request, 'admin.html')


def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'create_patient.html')

def medecin(request):
    return render(request, "medecin.html")

def infirmier(request):
    if request.method == "POST":
        type = request.POST.get('type')
        date = request.POST.get('date')
        description = request.POST.get('description')
        observation = request.POST.get('observation')
        nss = request.POST.get('nss')

      
        dossier = DossierPatient.objects.get(num_securite_sociale=nss)

        
        Soin.objects.create(
            date=date,
            type=type,
            description=description,
            observation=observation,
            infirmier_id=request.user.infirmier, 
            dossier_id=dossier.id,  
        )

        return redirect('soin_created')
    return render(request, "soins.html")

def soinCreated(request):
 return render(request, "soins_created.html")

def laborantin(request):
    return render(request, "laborantin.html")

def radiologue(request):
    return render(request, "radiologue.html")

def error(request):
    return render(request, "error404.html")


    

def authentification(request):

    if request.method == "POST":
        role = request.POST.get('role')
        username = request.POST.get("username")
        password = request.POST.get("password")

        if role == 'admin' and username == "fatima" and password == "123":
            return redirect('Admin') 
        elif role == 'patient':
         try:
           user = Patient.objects.get(user__email=username) 
           if user.user.check_password(password) :
              return redirect('success')
         except Patient.DoesNotExist:
              return redirect('error')
        elif role == 'medecin':
         try:
           user = Medecin.objects.get(user__email=username) 
           if user.user.check_password(password) :
              return redirect('medecin')
         except Medecin.DoesNotExist:
              return redirect('error')
        elif role == 'infirmier':
         try:
           user = Infirmier.objects.get(user__email=username) 
           if user.user.check_password(password) :
              return redirect('infirmier')
         except Infirmier.DoesNotExist:
              return redirect('error')
        elif role == 'laborantin':
         try:
           user = Laborantin.objects.get(user__email=username) 
           if user.user.check_password(password) :
              return redirect('laborantin')
         except Laborantin.DoesNotExist:
              return redirect('error')
        elif role == 'radiologue':
         try:
           user = Radiologue.objects.get(user__email=username) 
           if user.user.check_password(password) :
              return redirect('radiologue')
         except Radiologue.DoesNotExist:
              return redirect('error')

    return render(request, "authentification.html")