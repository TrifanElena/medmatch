from django.db import models
from clinics.models import Clinic
from services.models import MedicalSpecialty
from users.models import User

class Review(models.Model):
    appointment = models.OneToOneField('appointments.Appointment', on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f"Review pentru {self.appointment.clinic.name} - {self.rating}/10"