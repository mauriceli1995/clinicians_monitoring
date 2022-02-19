from django.db import models

# Create your models here.
from users.models import Patient

class Alert(models.Model):
    abnormal_found = models.BooleanField(default = False)
    patient = models.OneToOneField('users.Patient', on_delete=models.CASCADE)