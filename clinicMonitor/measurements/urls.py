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
]