from django.urls import path

from app import admin

from . import views  # Import views from your application

app_name = 'app'
urlpatterns = [
    path('admin/', admin.admin.site.urls),  # Admin site
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
    path('ordonnances/', views.OrdonnanceListView.as_view(), name='ordonnance_list'),  # List ordonnances
    path('ordonnances/<int:pk>/', views.OrdonnanceDetailView.as_view(), name='ordonnance_detail'),
    path('ordonnances/<int:pk>/delete/', views.DeleteOrdonnanceView.as_view(), name='ordonnance_delete'),
    path('medecins/<int:id>/', views.medecin_detail, name='medecin_detail'),
    path('medecins/<int:id>/delete/', views.medecin_destroy, name='medecin_delete'),
    path('medecin/search/<str:nss>/', views.SearchPatientView.as_view(), name='search_patient'),
    path('medecin/patients/', views.MedecinPatientList.as_view(), name='medecin_patient_list'),
    path('medecin/patients/<int:id>/', views.MedecinPatientDetail.as_view(), name='medecin_patient_detail'),
    path('medecin/patient/<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('medecin/consultation/create/', views.CreateConsultationView.as_view(), name='create_consultation'),
    path('medecin/consultation/list/', views.ConsultationListView.as_view(), name='consultation_list'),
    path('medecin/consultation/update/<int:pk>/',views.UpdateConsultationView.as_view(), name='update_consultation'),
    path('medecin/consultation/delete/<int:pk>/', views.DeleteConsultationView.as_view(), name='delete_consultation'),
    path('medecin/ordonnance/add/', views.AddOrdonnanceView.as_view(), name='add_ordonnance'),
    path('medecin/ordonnance/list/', views.OrdonnanceListView.as_view(), name='ordonnance_list'),
    path('medecin/ordonnance/update/<int:pk>/', views.UpdateOrdonnanceView.as_view(), name='update_ordonnance'),
    path('medecin/ordonnance/delete/<int:pk>/', views.DeleteOrdonnanceView.as_view(), name='delete_ordonnance'),
    path('medecin/exam/request/', views.RequestMedicalExamView.as_view(), name='request_exam'),
    path('medecin/exam/list/', views.MedicalExamListView.as_view(), name='exam_list'),
    path('medecin/exam/update/<int:pk>/', views.UpdateMedicalExamView.as_view(), name='update_exam'),
    path('medecin/exam/delete/<int:pk>/', views.DeleteMedicalExamView.as_view(), name='delete_exam'),
    path('examens/radiologiques/', views.ExamenRadiologiqueListView.as_view(), name='examen_radiologique_list'),
    path('examens/radiologiques/<int:pk>/', views.ExamenRadiologiqueDetailView.as_view(), name='examen_radiologique_detail'),
    path('examens/radiologiques/<int:pk>/delete/', views.DeleteExamenRadiologiqueView.as_view(), name='delete_examen_radiologique'),
    path('examens/biologiques/', views.ExamenBiologiqueListView.as_view(), name='examen_biologique_list'),
    path('examens/biologiques/<int:pk>/', views.ExamenBiologiqueDetailView.as_view(), name='examen_biologique_detail'),
    path('examens/biologiques/<int:pk>/delete/', views.DeleteExamenBiologiqueView.as_view(), name='delete_examen_biologique'),
    path('comptes_rendus/', views.CompteRenduListView.as_view(), name='compte_rendu_list'),
    path('comptes_rendus/<int:pk>/', views.CompteRenduDetailView.as_view(), name='compte_rendu_detail'),
    path('comptes_rendus/<int:pk>/delete/', views.DeleteCompteRenduView.as_view(), name='delete_compte_rendu'),
    path('medicaments/', views.MedicamentListView.as_view(), name='medicament_list'),
    path('medicaments/<int:pk>/', views.MedicamentDetailView.as_view(), name='medicament_detail'),
    path('medicaments/<int:pk>/delete/', views.DeleteMedicamentView.as_view(), name='delete_medicament'),
    path('ordonnances/medicaments/', views.OrdonnanceMedicamentListView.as_view(), name='ordonnance_medicament_list'),
    path('ordonnances/medicaments/<int:pk>/', views.OrdonnanceMedicamentDetailView.as_view(), name='ordonnance_medicament_detail'),
    path('ordonnances/medicaments/<int:pk>/delete/', views.DeleteOrdonnanceMedicamentView.as_view(), name='delete_ordonnance_medicament'),
    path('certificats_medicaux/', views.CertificatMedicalListView.as_view(), name='certificat_medical_list'),
    path('certificats_medicaux/<int:pk>/', views.CertificatMedicalDetailView.as_view(), name='certificat_medical_detail'),
    path('certificats_medicaux/<int:pk>/delete/', views.DeleteCertificatMedicalView.as_view(), name='delete_certificat_medical'),
    path('soins/', views.SoinListView.as_view(), name='soin_list'),
    path('soins/<int:pk>/', views.SoinDetailView.as_view(), name='soin_detail'),
    path('soins/<int:pk>/delete/', views.DeleteSoinView.as_view(), name='delete_soin'),
]

