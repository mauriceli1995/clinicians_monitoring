from django.urls import path

from . import views

app_name = 'measurements'
urlpatterns = [
    # ex: /measurements/fillInMeasurementPage/1/
    path('fillInMeasurementPage/<int:patient_id>/', views.fillInMeasurementPage, name='fillInMeasurementPage'),
    # ex: /measurements/submitMeasurement/1/
    path('submitMeasurement/<int:patient_id>/', views.submitMeasurement, name='submitMeasurement'),
    # ex: /measurements/submitMeasurementSuccess/1/
    path('submitMeasurementSuccess/<int:patient_id>/', views.submitMeasurementSuccess, name='submitMeasurementSuccess'),
    # ex: /measurements/patientViewMeasurement/1/
    path('patientViewMeasurement/<int:patient_id>/', views.patientViewMeasurement, name='patientViewMeasurement'),
    # ex: /measurements/clinicianViewMeasurement/1/
    path('clinicianViewMeasurement/<int:clinician_id>/', views.clinicianViewMeasurement, name='clinicianViewMeasurement'),
]