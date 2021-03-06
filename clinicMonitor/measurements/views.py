from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Measurement
from users.models import Patient, Clinician
from alerts.views import checkAbnormalReading, checkAbnormalReadingEmail

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
            patient = Patient.objects.get(pk=patient_id)
            clinician_id = patient.clinician_id
            checkAbnormalReadingEmail(request, patient_id, clinician_id)
            return HttpResponseRedirect(reverse('measurements:patientViewMeasurement', args=(patient_id,))) 
    else:
        return render(request,'measurements/fillInMeasurementPage.html')

def patientViewMeasurement(request, patient_id):
    selected_measurement_list = Measurement.objects.filter(patient = patient_id)
    measurement_list = selected_measurement_list.order_by('-submitted_date')
    patient = Patient.objects.get(pk=patient_id)
    context = {'measurement_list': measurement_list, 'patient_id': patient_id, 'patient_name': patient.patient_name}
    return render(request, 'measurements/patientViewMeasurement.html', context)

def clinicianViewMeasurements(request, clinician_id):
    clinician = Clinician.objects.get(pk = clinician_id)
    patient_list = Patient.objects.filter(clinician = clinician_id).values_list('id', flat=True)
    result_list = {}
    abnormal_patient_list = []
    for patient_id in patient_list:
        patient_name = Patient.objects.get(pk = patient_id)
        # check whether abnormal reading exists
        if checkAbnormalReading(request, patient_id) == True:
            abnormal_patient_list.append(patient_name)
        measurement_list = Measurement.objects.filter(patient = patient_id).order_by('-submitted_date')[:1]
        result_list[patient_name] = measurement_list
    context = {'abnormal_patient_list': abnormal_patient_list, 'result_list': result_list, 'clinician_name': clinician.clinician_name, 'clinician_id': clinician_id}
    return render(request, 'measurements/clinicianViewMeasurements.html', context)

def clinicianViewPatientDetail(request, clinician_id, patient_id):
    clinician = Clinician.objects.get(pk = clinician_id)
    selected_measurement_list = Measurement.objects.filter(patient = patient_id)
    measurement_list = selected_measurement_list.order_by('-submitted_date')
    patient = Patient.objects.get(pk=patient_id)
    context = {'measurement_list': measurement_list, 'patient_name': patient.patient_name, 'patient_id': patient_id, 'clinician_id': clinician_id}
    return render(request, 'measurements/clinicianViewPatientDetail.html', context)