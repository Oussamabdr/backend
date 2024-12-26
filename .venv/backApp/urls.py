from django.urls import path
from . import views  # Import views from your application

app_name = 'backApp'
urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),  # List patients
    path('patients/<int:id>/', views.patient_detail, name='patient_detail'), # Patient details by ID
    path('patients/<int:id>/delete/', views.patient_destroy, name='patient_delete'),
    path('medecins/', views.medecin_list, name='medecin_list'),  # List medecins
    path('pharmaciens/', views.pharmacien_list, name='pharmacien_list'),  # List pharmacien
    path('pharmaciens/<int:id>/', views.pharmacien_detail, name='pharmacien_detail'),
    path('pharmaciens/<int:id>/delete/', views.pharmacien_destroy, name='pharmacien_delete'),
    path('radiologues/', views.radiologue_list, name='radiologue_list'),  # List radiologue
    path('radiologues/<int:id>/', views.radiologue_detail, name='radiologue_detail'),
    path('radiologues/<int:id>/delete/', views.radiologue_destroy, name='radiologue_delete'),
    path('infirmiers/', views.infirmier_list, name='infirmier_list'),  # List infirmier
    path('infirmiers/<int:id>/', views.infirmier_detail, name='infirmier_detail'),
    path('infirmiers/<int:id>/delete/', views.infirmier_destroy, name='infirmier_delete'),
    path('examens/', views.examen_list, name='examen_list'),  # List examens
    path('examens/<int:id>/', views.examen_detail, name='examen_detail'),
    path('examens/<int:id>/delete/', views.examen_destroy, name='examen_delete'),
    path('prescriptions/', views.prescription_list, name='prescription_list'),  # List prescriptions
    path('prescriptions/<int:id>/', views.prescription_detail, name='prescription_detail'),
    path('prescriptions/<int:id>/delete/', views.prescription_destroy, name='prescription_delete'),
    path('medecins/<int:id>/', views.medecin_detail, name='medecin_detail'),
    path('medecins/<int:id>/delete/', views.medecin_destroy, name='medecin_delete'),
    path('medecin/search/<str:nss>/', views.SearchPatientView.as_view(), name='search_patient'),
    path('medecin/patient/<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('medecin/consultation/create/', views.CreateConsultationView.as_view(), name='create_consultation'),
    path('medecin/consultation/list/', views.ConsultationListView.as_view(), name='consultation_list'),
    path('medecin/consultation/update/<int:pk>/',views.UpdateConsultationView.as_view(), name='update_consultation'),
    path('medecin/consultation/delete/<int:pk>/', views.DeleteConsultationView.as_view(), name='delete_consultation'),
    path('medecin/prescription/add/', views.AddPrescriptionView.as_view(), name='add_prescription'),
    path('medecin/prescription/list/', views.PrescriptionListView.as_view(), name='prescription_list'),
    path('medecin/prescription/update/<int:pk>/', views.UpdatePrescriptionView.as_view(), name='update_prescription'),
    path('medecin/prescription/delete/<int:pk>/', views.DeletePrescriptionView.as_view(), name='delete_prescription'),
    path('medecin/exam/request/', views.RequestMedicalExamView.as_view(), name='request_exam'),
    path('medecin/exam/list/', views.MedicalExamListView.as_view(), name='exam_list'),
    path('medecin/exam/update/<int:pk>/', views.UpdateMedicalExamView.as_view(), name='update_exam'),
    path('medecin/exam/delete/<int:pk>/', views.DeleteMedicalExamView.as_view(), name='delete_exam'),
 

]

