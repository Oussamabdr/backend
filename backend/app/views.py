from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView,CreateAPIView,UpdateAPIView,ListAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .user_serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWithRoleSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWithRoleSerializer
    permission_classes = [IsAdminOrReadOnly]
# Create your views here.
'''
@api_view(['GET', 'POST'])
@csrf_exempt
def patient_list(request):
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def patient_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        patient = Patient.objects.get(pk=id)
        return JsonResponse(model_to_dict(patient))
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def patient_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        patient = Patient.objects.get(pk=id)
        patient.delete()
        return JsonResponse({'message': 'Patient deleted'}, status=200)
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def medecin_list(request):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    medecins = list(Medecin.objects.all())
    medecin_dicts = [model_to_dict(medecin) for medecin in medecins]
    return JsonResponse(medecin_dicts, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def medecin_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        medecin = Medecin.objects.get(pk=id)
        return JsonResponse(model_to_dict(medecin))
    except Medecin.DoesNotExist:
        return JsonResponse({'error': 'Medecin not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def medecin_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        medecin = Medecin.objects.get(pk=id)
        medecin.delete()
        return JsonResponse({'message': 'Medecin deleted'}, status=200)
    except Medecin.DoesNotExist:
        return JsonResponse({'error': 'Medecin not found'}, status=404)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def medecin_list_patients(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        medecin = Medecin.objects.get(pk=id)
        patients = medecin.patients.all()
        patient_dicts = [model_to_dict(patient) for patient in patients]
        return JsonResponse(patient_dicts, safe=False)
    except Medecin.DoesNotExist:
        return JsonResponse({'error': 'Medecin not found'}, status=404)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def pharmacien_list(request):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    pharmaciens = list(Pharmacien.objects.all())
    pharmacien_dicts = [model_to_dict(pharmacien) for pharmacien in pharmaciens]
    return JsonResponse(pharmacien_dicts, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def pharmacien_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        pharmacien = Pharmacien.objects.get(pk=id)
        return JsonResponse(model_to_dict(pharmacien))
    except Pharmacien.DoesNotExist:
        return JsonResponse({'error': 'Pharmacien not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def pharmacien_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        pharmacien = Pharmacien.objects.get(pk=id)
        pharmacien.delete()
        return JsonResponse({'message': 'Pharmacien deleted'}, status=200)
    except Pharmacien.DoesNotExist:
        return JsonResponse({'error': 'Pharmacien not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def radiologue_list(request):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    radiologues = list(Radiologue.objects.all())
    radiologue_dicts = [model_to_dict(radiologue) for radiologue in radiologues]
    return JsonResponse(radiologue_dicts, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def radiologue_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        radiologue = Radiologue.objects.get(pk=id)
        return JsonResponse(model_to_dict(radiologue))
    except Radiologue.DoesNotExist:
        return JsonResponse({'error': 'Radiologue not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def radiologue_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        radiologue = Radiologue.objects.get(pk=id)
        radiologue.delete()
        return JsonResponse({'message': 'Radiologue deleted'}, status=200)
    except Radiologue.DoesNotExist:
        return JsonResponse({'error': 'Radiologue not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def radiologue_list_examens(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        radiologue = Radiologue.objects.get(pk=id)
        examens = radiologue.examens.all()
        examen_dicts = [model_to_dict(examen) for examen in examens]
        return JsonResponse(examen_dicts, safe=False)
    except Radiologue.DoesNotExist:
        return JsonResponse({'error': 'Radiologue not found'}, status=404)
    
    

@csrf_exempt
@require_http_methods(["GET", "POST"])
def ordonance_list(request):
    
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    ordonnances = list(Ordonnance.objects.all())
    ordonnance_dicts = [model_to_dict(ord) for ordonnance in ordonnances]
    return JsonResponse(ordonnance_dicts, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def ordonnance_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        ordonnance = Ordonnance.objects.get(pk=id)
        return JsonResponse(model_to_dict(ordonnance))
    except Ordonnance.DoesNotExist:
        return JsonResponse({'error': 'Ordonnance not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def ordonnance_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        ordonnance = Ordonnance.objects.get(pk=id)
        ordonnance.delete()
        return JsonResponse({'message': 'Ordonnance deleted'}, status=200)
    except Ordonnance.DoesNotExist:
        return JsonResponse({'error': 'Ordonnance not found'}, status=404)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def examen_list(request):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    examens = list(Examen.objects.all())
    examen_dicts = [model_to_dict(examen) for examen in examens]
    return JsonResponse(examen_dicts, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def examen_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        examen = Examen.objects.get(pk=id)
        return JsonResponse(model_to_dict(examen))
    except Examen.DoesNotExist:
        return JsonResponse({'error': 'Examen not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def examen_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        examen = Examen.objects.get(pk=id)
        examen.delete()
        return JsonResponse({'message': 'Examen deleted'}, status=200)
    except Examen.DoesNotExist:
        return JsonResponse({'error': 'Examen not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def laborantin_list(request):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    laborantins = list(Laborantin.objects.all())
    laborantin_dicts = [model_to_dict(laborantin) for laborantin in laborantins]
    return JsonResponse(laborantin_dicts, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def laborantin_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        laborantin = Laborantin.objects.get(pk=id)
        return JsonResponse(model_to_dict(laborantin))
    except Laborantin.DoesNotExist:
        return JsonResponse({'error': 'Laborantin not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def laborantin_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        laborantin = Laborantin.objects.get(pk=id)
        laborantin.delete()
        return JsonResponse({'message': 'Laborantin deleted'}, status=200)
    except Laborantin.DoesNotExist:
        return JsonResponse({'error': 'Laborantin not found'}, status=404)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def infirmier_list(request):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    infirmiers = list(Infirmier.objects.all())
    infirmier_dicts = [model_to_dict(infirmier) for infirmier in infirmiers]
    return JsonResponse(infirmier_dicts, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def infirmier_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        infirmier = Infirmier.objects.get(pk=id)
        return JsonResponse(model_to_dict(infirmier))
    except Infirmier.DoesNotExist:
        return JsonResponse({'error': 'Infirmier not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def infirmier_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        infirmier = Infirmier.objects.get(pk=id)
        infirmier.delete()
        return JsonResponse({'message': 'Infirmier deleted'}, status=200)
    except Infirmier.DoesNotExist:
        return JsonResponse({'error': 'Infirmier not found'}, status=404)


class SearchPatientView(APIView):
    def get(self, request, nss):
        try:
            patient = Patient.objects.get(nss=nss)
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

'''
class ListConsultationView(ListAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class CreateConsultationView(CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class UpdateConsultationView(UpdateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class DeleteConsultationView(DestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class AddOrdonnanceView(CreateAPIView):
    queryset = Ordonnance.objects.all()
    serializer_class =  OrdonnanceSerializer

class ListOrdonnanceView(ListAPIView):
    queryset = Ordonnance.objects.all()
    serializer_class = OrdonnanceSerializer

class DeleteOrdonnanceView(DestroyAPIView):
    queryset = Ordonnance.objects.all()
    serializer_class = OrdonnanceSerializer
'''
class ListExamenView(ListAPIView):
    serializer_class = ExamenSerializer

    def get_queryset(self):
        """
        This view should return a list of all exams
        for the currently authenticated user.
        """
        user = self.request.user
        return Examen.objects.filter(medecin=user)

class CreateExamenView(CreateAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class UpdateExamenView(UpdateAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class DeleteExamenView(DestroyAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer


class ExamenDetailView(RetrieveAPIView):
    serializer_class = ExamenSerializer
    queryset = Examen.objects.all()'''

class ExamenRadiologiqueListCreateView(CreateAPIView):
    queryset = ExamenRadiologique.objects.all()
    serializer_class = ExamenRadiologiqueSerializer

# View for retrieving, updating, and deleting ExamenRadiologique
class ExamenRadiologiqueDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ExamenRadiologique.objects.all()
    serializer_class = ExamenRadiologiqueSerializer

# View for listing and creating ExamenBiologique
class ExamenBiologiqueListCreateView(ListCreateAPIView):
    queryset = ExamenBiologique.objects.all()
    serializer_class = ExamenBiologiqueSerializer

# View for retrieving, updating, and deleting ExamenBiologique
class ExamenBiologiqueDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ExamenBiologique.objects.all()
    serializer_class = ExamenBiologiqueSerializer



class ListInfirmierView(ListAPIView):
    queryset = Infirmier.objects.all()
    serializer_class = InfirmierSerializer

class CreateInfirmierView(CreateAPIView):
    queryset = Infirmier.objects.all()
    serializer_class = InfirmierSerializer

class UpdateInfirmierView(UpdateAPIView):
    queryset = Infirmier.objects.all()
    serializer_class = InfirmierSerializer

class DeleteInfirmierView(DestroyAPIView):
    queryset = Infirmier.objects.all()
    serializer_class = InfirmierSerializer


class ListPharmacienView(ListAPIView):
    queryset = Pharmacien.objects.all()
    serializer_class = PharmacienSerializer

class CreatePharmacienView(CreateAPIView):
    queryset = Pharmacien.objects.all()
    serializer_class = PharmacienSerializer

class UpdatePharmacienView(UpdateAPIView):
    queryset = Pharmacien.objects.all()
    serializer_class = PharmacienSerializer

class DeletePharmacienView(DestroyAPIView):
    queryset = Pharmacien.objects.all()
    serializer_class = PharmacienSerializer


class ListRadiologueView(ListAPIView):
    queryset = Radiologue.objects.all()
    serializer_class = RadiologueSerializer

class CreateRadiologueView(CreateAPIView):
    queryset = Radiologue.objects.all()
    serializer_class = RadiologueSerializer

class UpdateRadiologueView(UpdateAPIView):
    queryset = Radiologue.objects.all()
    serializer_class = RadiologueSerializer

class DeleteRadiologueView(DestroyAPIView):
    queryset = Radiologue.objects.all()
    serializer_class = RadiologueSerializer

class ListAntecedentView(ListAPIView):
    queryset = Antecedent.objects.all()
    serializer_class = AntecedentSerializer

class CreateAntecedentView(CreateAPIView):
    queryset = Antecedent.objects.all()
    serializer_class = AntecedentSerializer

class UpdateAntecedentView(UpdateAPIView):
    queryset = Antecedent.objects.all()
    serializer_class = AntecedentSerializer

class DeleteAntecedentView(DestroyAPIView):
    queryset = Antecedent.objects.all()
    serializer_class = AntecedentSerializer

class ListDossierPatientView(ListAPIView):
    queryset = DossierPatient.objects.all()
    serializer_class = DossierPatientSerializer

class CreateDossierPatientView(CreateAPIView):
    queryset = DossierPatient.objects.all()
    serializer_class = DossierPatientSerializer

class UpdateDossierPatientView(UpdateAPIView):
    queryset = DossierPatient.objects.all()
    serializer_class = DossierPatientSerializer

class DeleteDossierPatientView(DestroyAPIView):
    queryset = DossierPatient.objects.all()
    serializer_class = DossierPatientSerializer


class ListCompteRenduView(ListAPIView):
    queryset = CompteRendu.objects.all()
    serializer_class = CompteRenduSerializer

class CreateCompteRenduView(CreateAPIView):
    queryset = CompteRendu.objects.all()
    serializer_class = CompteRenduSerializer

class UpdateCompteRenduView(UpdateAPIView):
    queryset = CompteRendu.objects.all()
    serializer_class = CompteRenduSerializer

class DeleteCompteRenduView(DestroyAPIView):
    queryset = CompteRendu.objects.all()
    serializer_class = CompteRenduSerializer


class ListMedicamentView(ListAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer

class CreateMedicamentView(CreateAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer

class UpdateMedicamentView(UpdateAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer

class DeleteMedicamentView(DestroyAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer


class ListOrdonnanceMedicamentView(ListAPIView):
    queryset = OrdonnanceMedicament.objects.all()
    serializer_class = OrdonnanceMedicamentSerializer

class CreateOrdonnanceMedicamentView(CreateAPIView):
    queryset = OrdonnanceMedicament.objects.all()
    serializer_class = OrdonnanceMedicamentSerializer

class UpdateOrdonnanceMedicamentView(UpdateAPIView):
    queryset = OrdonnanceMedicament.objects.all()
    serializer_class = OrdonnanceMedicamentSerializer

class DeleteOrdonnanceMedicamentView(DestroyAPIView):
    queryset = OrdonnanceMedicament.objects.all()
    serializer_class = OrdonnanceMedicamentSerializer


class ListCertificatMedicalView(ListAPIView):
    queryset = CertificatMedical.objects.all()
    serializer_class = CertificatMedicalSerializer

class CreateCertificatMedicalView(CreateAPIView):
    queryset = CertificatMedical.objects.all()
    serializer_class = CertificatMedicalSerializer

class UpdateCertificatMedicalView(UpdateAPIView):
    queryset = CertificatMedical.objects.all()
    serializer_class = CertificatMedicalSerializer

class DeleteCertificatMedicalView(DestroyAPIView):
    queryset = CertificatMedical.objects.all()
    serializer_class = CertificatMedicalSerializer


class ListSoinView(ListAPIView):
    queryset = Soin.objects.all()
    serializer_class = SoinSerializer

class CreateSoinView(CreateAPIView):
    queryset = Soin.objects.all()
    serializer_class = SoinSerializer

class UpdateSoinView(UpdateAPIView):
    queryset = Soin.objects.all()
    serializer_class = SoinSerializer

class DeleteSoinView(DestroyAPIView):
    queryset = Soin.objects.all()
    serializer_class = SoinSerializer

class CompteRenduDetailView(RetrieveAPIView):
    serializer_class = CompteRenduSerializer
    queryset = CompteRendu.objects.all()

class MedicamentDetailView(RetrieveAPIView):
    serializer_class = MedicamentSerializer
    queryset = Medicament.objects.all()

class OrdonnanceMedicamentDetailView(RetrieveAPIView):
    serializer_class = OrdonnanceMedicamentSerializer
    queryset = OrdonnanceMedicament.objects.all()

class CertificatMedicalDetailView(RetrieveAPIView):
    serializer_class = CertificatMedicalSerializer
    queryset = CertificatMedical.objects.all()

class SoinDetailView(RetrieveAPIView):
    serializer_class = SoinSerializer
    queryset = Soin.objects.all()

class MedecinPatientList(ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        """
        This view should return a list of all patients
        ford the currently authenticated user.
        """
        user = self.request.user
        return Patient.objects.filter(medecin=user)
    
class MedecinPatientDetail(RetrieveAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class PatientDetailView(RetrieveAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class ListPatientView(ListAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class CreatePatientView(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class UpdatePatientView(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DeletePatientView(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class OrdonnanceListView(ListAPIView):
    serializer_class = OrdonnanceSerializer

    def get_queryset(self):
        """
        This view should return a list of all ordonnances
        for the currently authenticated user.
        """
        user = self.request.user
        return Ordonnance.objects.filter(medecin=user)

class OrdonnanceDetailView(RetrieveAPIView):
    serializer_class = OrdonnanceSerializer
    queryset = Ordonnance.objects.all()

class OrdonnanceDeleteView(DestroyAPIView):
    serializer_class = OrdonnanceSerializer
    queryset = Ordonnance.objects.all()
class ConsultationListView(ListAPIView):
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        """
        This view should return a list of all consultations
        for the currently authenticated user.
        """
        user = self.request.user
        return Consultation.objects.filter(medecin=user)
class UpdateOrdonnanceView(UpdateAPIView):
    queryset = Ordonnance.objects.all()
    serializer_class = OrdonnanceSerializer



class CompteRenduListView(ListAPIView):
    serializer_class = CompteRenduSerializer

    def get_queryset(self):
        """
        This view should return a list of all compte rendus
        for the currently authenticated user.
        """
        user = self.request.user
        return CompteRendu.objects.filter(auteur=user)
class MedicamentListView(ListAPIView):
    serializer_class = MedicamentSerializer
    queryset = Medicament.objects.all()

class OrdonnanceMedicamentListView(ListAPIView):
    serializer_class = OrdonnanceMedicamentSerializer

    def get_queryset(self):
        """
        This view should return a list of all ordonnances medicaments
        for the currently authenticated user.
        """
        user = self.request.user
        return OrdonnanceMedicament.objects.filter(ordonnance__medecin=user)

class CertificatMedicalListView(ListAPIView):
    serializer_class = CertificatMedicalSerializer

    def get_queryset(self):
        """
        This view should return a list of all certificats medicaux
        for the currently authenticated user.
        """
        user = self.request.user
        return CertificatMedical.objects.filter(dossier__patient=user)

class SoinListView(ListAPIView):
    serializer_class = SoinSerializer

    def get_queryset(self):
        """
        This view should return a list of all soins
        for the currently authenticated user.
        """
        user = self.request.user
        return Soin.objects.filter(infirmier=user)
