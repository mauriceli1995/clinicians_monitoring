from django.urls import path

from . import views

app_name = 'measurements'
urlpatterns = [
    # ex: /measurements/fillInMeasurementPage/1/
    path('fillInMeasurementPage/<int:patient_id>/', views.fillInMeasurementPage, name='fillInMeasurementPage'),
    # ex: /measurements/submitMeasurement/1/
    path('submitMeasurement/<int:patient_id>/', views.submitMeasurement, name='submitMeasurement'),
    # ex: /measurements/patientViewMeasurement/1/
    path('patientViewMeasurement/<int:patient_id>/', views.patientViewMeasurement, name='patientViewMeasurement'),
    # ex: /measurements/clinicianViewMeasurements/1/
    path('clinicianViewMeasurements/<int:clinician_id>/', views.clinicianViewMeasurements, name='clinicianViewMeasurements'),
    # ex: /measurements/clinicianViewPatientDetail/1/1/
    path('clinicianViewPatientDetail/<int:clinician_id>/<int:patient_id>/', views.clinicianViewPatientDetail, name='clinicianViewPatientDetail'),
]