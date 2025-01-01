from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView,CreateAPIView,UpdateAPIView,ListAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .user_serializer import UserWithRoleSerializer,IsAdminOrReadOnly ,PatientSerializer,PatientDetailSerializer,MedecinSerializer,PharmacienSerializer,InfirmierSerializer,TechnicienSerializer,RadiologueSerializer,InfirmierSerializer
from .models import Patient , Medecin, Pharmacien, Infirmier, Technicien, Radiologue, Prescription, Examen,Consultation,Prescription,Infirmier
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ConsultationSerializer,PrescriptionSerializer,ExamenSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWithRoleSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWithRoleSerializer
    permission_classes = [IsAdminOrReadOnly]
# Create your views here.
from django.forms.models import model_to_dict



from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods

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
def prescription_list(request):
    
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    prescriptions = list(Prescription.objects.all())
    prescription_dicts = [model_to_dict(prescription) for prescription in prescriptions]
    return JsonResponse(prescription_dicts, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def prescription_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        prescription = Prescription.objects.get(pk=id)
        return JsonResponse(model_to_dict(prescription))
    except Prescription.DoesNotExist:
        return JsonResponse({'error': 'Prescription not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def prescription_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        prescription = Prescription.objects.get(pk=id)
        prescription.delete()
        return JsonResponse({'message': 'Prescription deleted'}, status=200)
    except Prescription.DoesNotExist:
        return JsonResponse({'error': 'Prescription not found'}, status=404)


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
def technicien_list(request):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    techniciens = list(Technicien.objects.all())
    technicien_dicts = [model_to_dict(technicien) for technicien in techniciens]
    return JsonResponse(technicien_dicts, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def technicien_detail(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        technicien = Technicien.objects.get(pk=id)
        return JsonResponse(model_to_dict(technicien))
    except Technicien.DoesNotExist:
        return JsonResponse({'error': 'Technicien not found'}, status=404)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def technicien_destroy(request, id):
    if request.method == 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        technicien = Technicien.objects.get(pk=id)
        technicien.delete()
        return JsonResponse({'message': 'Technicien deleted'}, status=200)
    except Technicien.DoesNotExist:
        return JsonResponse({'error': 'Technicien not found'}, status=404)


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

class PatientDetailView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer  

class CreateConsultationView(CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class AddPrescriptionView(CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class RequestExamenView(CreateAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class UpdateConsultationView(UpdateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ListConsultationView(ListAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ListPrescriptionView(ListAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class ListExamenView(ListAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class DeletePrescriptionView(DestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class DeleteMedicalExamView(DestroyAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class DeleteConsultationView(DestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class RequestMedicalExamView(CreateAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

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
