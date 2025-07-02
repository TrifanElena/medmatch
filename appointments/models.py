#appointments/models.py
from django.db import models
from users.models import User
from django.conf import settings
from clinics.models import Clinic
from services.models import MedicalSpecialty

class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE,  related_name='appointments')
    specialty = models.ForeignKey(MedicalSpecialty, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    fulfilled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.clinic.name} - {self.date} {self.time}"
