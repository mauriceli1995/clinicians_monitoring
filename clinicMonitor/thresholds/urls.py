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
]