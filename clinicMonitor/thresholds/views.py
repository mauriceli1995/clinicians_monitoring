from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from measurements.models import Measurement
from users.models import Patient, Clinician
from .models import Threshold

def setThresholdsPage(request, patient_id):
    context = {'patient_id': patient_id}
    return render(request, 'thresholds/setThresholdsPage.html', context)

def submitThreshold(request, patient_id):
    if request.method == 'POST':
        patient = Patient.objects.get(pk=patient_id)
        clinician_id = patient.clinician_id
        if request.POST.get('maxHeartRate') and request.POST.get('minHeartRate') and request.POST.get('maxBloodPressure') and request.POST.get('minBloodPressure') and request.POST.get('maxBodyWeight') and request.POST.get('minBodyWeight'):
            if Threshold.objects.filter(patient = patient_id).exists():
                Threshold.objects.filter(patient = patient_id).update(
                    max_heart_rate = request.POST.get('maxHeartRate'),
                    min_heart_rate = request.POST.get('minHeartRate'),
                    max_blood_pressure = request.POST.get('maxBloodPressure'),
                    min_blood_pressure = request.POST.get('minBloodPressure'),
                    max_body_weight = request.POST.get('maxBodyWeight'),
                    min_body_weight = request.POST.get('minBodyWeight'),
                    setting_date = timezone.now())
                return HttpResponseRedirect(reverse('measurements:clinicianViewPatientDetail', args=(clinician_id, patient_id))) 
            else:
                threshold=Threshold()
                threshold.max_heart_rate = request.POST.get('maxHeartRate')
                threshold.min_heart_rate = request.POST.get('minHeartRate')
                threshold.max_blood_pressure = request.POST.get('maxBloodPressure')
                threshold.min_blood_pressure = request.POST.get('minBloodPressure')
                threshold.max_body_weight = request.POST.get('maxBodyWeight')
                threshold.min_body_weight = request.POST.get('minBodyWeight')
                threshold.setting_date = timezone.now()
                threshold.patient = Patient.objects.get(pk=patient_id)
                threshold.save()
                return HttpResponseRedirect(reverse('measurements:clinicianViewPatientDetail', args=(clinician_id, patient_id))) 
    else:
        return render(request,'thresholds/setThresholdsPage.html')