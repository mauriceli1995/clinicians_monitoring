from django.urls import path

from . import views

app_name = 'thresholds'
urlpatterns = [
    # ex: /thresholds/setThresholdsPage/1/
    path('setThresholdsPage/<int:patient_id>/', views.setThresholdsPage, name='setThresholdsPage'),
    # ex: /thresholds/submitMeasurement/1/
    path('submitThreshold/<int:patient_id>/', views.submitThreshold, name='submitThreshold'),
    # ex: /thresholds/submitMeasurementSuccess/1/
    path('settingThresholdSuccess/<int:patient_id>/', views.settingThresholdSuccess, name='settingThresholdSuccess'),
    # # ex: /measurements/patientViewMeasurement/1/
    # path('patientViewMeasurement/<int:patient_id>/', views.patientViewMeasurement, name='patientViewMeasurement'),
    # # ex: /measurements/clinicianViewMeasurements/1/
    # path('clinicianViewMeasurements/<int:clinician_id>/', views.clinicianViewMeasurements, name='clinicianViewMeasurements'),
    # # ex: /measurements/clinicianViewPatientDetail/1/1/
    # path('clinicianViewPatientDetail/<int:clinician_id>/<int:patient_id>/', views.clinicianViewPatientDetail, name='clinicianViewPatientDetail'),
]