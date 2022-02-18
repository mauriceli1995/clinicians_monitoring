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
]