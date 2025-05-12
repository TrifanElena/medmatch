from django.db import models

class MedicalSpecialty(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Medical Specialties"

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.ForeignKey(MedicalSpecialty, on_delete=models.CASCADE, related_name='symptoms')

    class Meta:
        verbose_name_plural = "Symptoms"

    def __str__(self):
        return self.name
