from django.db import models
from services.models import MedicalSpecialty

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True, null=True) 
    specialties = models.ManyToManyField('services.MedicalSpecialty', related_name='clinics')
    # specialty = models.ForeignKey('services.MedicalSpecialty', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
