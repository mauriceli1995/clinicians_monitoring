from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    # ex: /users/registerPatientPage/1/
    path('registerPatientPage/<int:clinician_id>/', views.registerPatientPage, name='registerPatientPage'),
    # ex: /users/registerPatient/1/
    path('registerPatient/<int:clinician_id>/', views.registerPatient, name='registerPatient'),
    # ex: /users/registerSuccess/1/
    path('registerSuccess/<int:clinician_id>/', views.registerSuccess, name='registerSuccess'),
    # ex: /users/clinicianLoginPage/
    path('clinicianLoginPage/', views.clinicianLoginPage, name='clinicianLoginPage'),
    # ex: /users/clinicianLoginProcess/
    path('clinicianLoginProcess/', views.clinicianLoginProcess, name='clinicianLoginProcess'),
    # ex: /users/clinicianLogout/1/
    path('clinicianLogout/<int:clinician_id>/', views.clinicianLogout, name='clinicianLogout'),
    # ex: /users/patientLoginPage/
    path('patientLoginPage/', views.patientLoginPage, name='patientLoginPage'),
    # ex: /users/patientLoginProcess/
    path('patientLoginProcess/', views.patientLoginProcess, name='patientLoginProcess'),
    # ex: /users/patientLogout/1/
    path('patientLogout/<int:patient_id>/', views.patientLogout, name='patientLogout'),
]