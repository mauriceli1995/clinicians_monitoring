from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Clinician, Patient


def registerPatientPage(request, clinician_id):
    context = {'clinician_id': clinician_id}
    return render(request, 'users/registerPatientPage.html', context)

def registerPatient(request, clinician_id):
    if request.method == 'POST':
        if request.POST.get('patientName') and request.POST.get('email') and (request.POST.get('psw') == request.POST.get('psw-repeat')):
            patient=Patient()
            patient.patient_name = request.POST.get('patientName')
            patient.email_address = request.POST.get('email')
            patient.password = request.POST.get('psw')
            patient.clinician = Clinician.objects.get(pk=clinician_id)
            patient.save()
            patient_id = patient.id
            return HttpResponseRedirect(reverse('thresholds:setThresholdsPage', args=(patient_id,))) 
    else:
        return render(request,'users/registerPatientPage.html')

def clinicianLoginPage(request):
    context = {}
    return render(request, 'users/clinicianLoginPage.html', context)

def clinicianLoginProcess(request):
    if request.method == 'POST':
        try:
            clinician = Clinician.objects.get(email_address = request.POST.get('email'), password = request.POST.get('psw'))
            clinician.auth_login = True
            clinician.save()
            clinician_id = clinician.id
            return HttpResponseRedirect(reverse('measurements:clinicianViewMeasurements', args=(clinician_id,))) 
        except:
            return HttpResponseRedirect(reverse('users:clinicianLoginPage'))

def clinicianLogout(request, clinician_id):
    clinician = Clinician.objects.get(pk = clinician_id)
    clinician.auth_login = False
    clinician.save()
    return HttpResponseRedirect(reverse('users:clinicianLoginPage')) 

def patientLoginPage(request):
    context = {}
    return render(request, 'users/patientLoginPage.html', context)

def patientLoginProcess(request):
    if request.method == 'POST':
        try:
            patient = Patient.objects.get(email_address = request.POST.get('email'), password = request.POST.get('psw'))
            patient.auth_login = True
            patient.save()
            patient_id = patient.id
            return HttpResponseRedirect(reverse('measurements:patientViewMeasurement', args=(patient_id,))) 
        except:
            return HttpResponseRedirect(reverse('users:patientLoginPage')) 

def patientLogout(request, patient_id):
    patient = Patient.objects.get(pk = patient_id)
    patient.auth_login = False
    patient.save()
    return HttpResponseRedirect(reverse('users:patientLoginPage')) 