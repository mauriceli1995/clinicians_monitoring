from django.db import models

# Create your models here.
from users.models import Patient

class Measurement(models.Model):
    heart_rate = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    body_weight = models.DecimalField(max_digits=5, decimal_places=2)
    submitted_date = models.DateTimeField('date submitted')
    patient = models.ForeignKey('users.Patient', on_delete=models.CASCADE)
    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.heart_rate, self.blood_pressure, self.body_weight, self.submitted_date, self.patient)