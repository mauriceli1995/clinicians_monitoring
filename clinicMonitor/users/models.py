from django.db import models

# Create your models here.

class Clinician(models.Model):
    clinician_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length = 254)
    password = models.CharField(max_length=200)
    auth_login = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s, %s' % (self.clinician_name, self.email_address, self.password)

class Patient(models.Model):
    patient_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length = 254)
    password = models.CharField(max_length=200)
    auth_login = models.BooleanField(default=False)
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE)
