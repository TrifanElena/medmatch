# from django.db import models
# from services.models import MedicalSpecialty

# class Clinic(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100, blank=True, null=True) 
#     specialties = models.ManyToManyField('services.MedicalSpecialty', related_name='clinics')
#     # specialty = models.ForeignKey('services.MedicalSpecialty', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

from django.db import models
from services.models import MedicalSpecialty
from django.contrib.auth.hashers import make_password, check_password

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)  # hashuit!
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True, null=True)
    specialties = models.ManyToManyField('services.MedicalSpecialty', related_name='clinics')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name
