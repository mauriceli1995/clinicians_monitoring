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
            return HttpResponseRedirect(reverse('users:registerSuccess', args=(clinician_id,))) 
    else:
        return render(request,'users/registerPatientPage.html')

def registerSuccess(request, clinician_id):
    return HttpResponse("Patient account created by %s" % clinician_id)