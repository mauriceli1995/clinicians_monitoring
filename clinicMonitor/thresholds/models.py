from django.db import models

# Create your models here.
from users.models import Patient

class Threshold(models.Model):
    min_heart_rate = models.DecimalField(max_digits=5, decimal_places=2)
    max_heart_rate = models.DecimalField(max_digits=5, decimal_places=2)
    min_blood_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    max_blood_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    min_body_weight = models.DecimalField(max_digits=5, decimal_places=2)
    max_body_weight = models.DecimalField(max_digits=5, decimal_places=2)
    setting_date = models.DateTimeField('setting date')
    patient = models.OneToOneField('users.Patient', on_delete=models.CASCADE)
