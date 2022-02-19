from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from measurements.models import Measurement
from users.models import Patient, Clinician
from thresholds.models import Threshold
from .models import Alert

def checkAbnormalReading(request, patient_id):
    got_alert_row = False
    if Alert.objects.filter(patient = patient_id).exists():
        got_alert_row = True
    patient = Patient.objects.get(pk=patient_id)
    measurement_list = Measurement.objects.filter(patient = patient_id).order_by('-submitted_date')[0]
    threshold_list = Threshold.objects.get(patient = patient_id)
    alert = Alert()
    if (threshold_list.min_heart_rate <= measurement_list.heart_rate <= threshold_list.max_heart_rate) and (threshold_list.min_blood_pressure <= measurement_list.blood_pressure <= threshold_list.max_blood_pressure) and (threshold_list.min_body_weight <= measurement_list.body_weight <= threshold_list.max_body_weight):
        if got_alert_row == False:
            alert.abnormal_found = False
            alert.patient = Patient.objects.get(pk=patient_id)
            alert.save()
        else:
            Alert.objects.filter(patient = patient_id).update(abnormal_found = False)
        return False
    elif got_alert_row == True:
        Alert.objects.filter(patient = patient_id).update(abnormal_found = True)
        return True
    elif got_alert_row == False:
        alert.abnormal_found = True
        alert.patient = Patient.objects.get(pk=patient_id)
        alert.save()
        return True