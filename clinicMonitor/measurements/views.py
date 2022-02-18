from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Measurement
from users.models import Patient

def fillInMeasurementPage(request, patient_id):
    context = {'patient_id': patient_id}
    return render(request, 'measurements/fillInMeasurementPage.html', context)

def submitMeasurement(request, patient_id):
    if request.method == 'POST':
        if request.POST.get('heartRate') and request.POST.get('bloodPressure') and request.POST.get('bodyWeight'):
            measurement=Measurement()
            measurement.heart_rate = request.POST.get('heartRate')
            measurement.blood_pressure = request.POST.get('bloodPressure')
            measurement.body_weight = request.POST.get('bodyWeight')
            measurement.submitted_date = timezone.now()
            measurement.patient = Patient.objects.get(pk=patient_id)
            measurement.save()
            return HttpResponseRedirect(reverse('measurements:submitMeasurementSuccess', args=(patient_id,))) 
    else:
        return render(request,'measurements/fillInMeasurementPage.html')

def submitMeasurementSuccess(request, patient_id):
    return HttpResponse("Measurement submitted by patient %s" % patient_id)