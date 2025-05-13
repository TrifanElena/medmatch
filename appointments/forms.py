from django import forms
from .models import Appointment
from services.models import MedicalSpecialty

# class AppointmentForm(forms.ModelForm):
#     specialty = forms.ModelChoiceField(queryset=MedicalSpecialty.objects.all(), required=True)


#     class Meta:
#         model = Appointment
#         fields = ['clinic', 'specialty', 'date', 'time']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'time': forms.TimeInput(attrs={'type': 'time'}),
#         }

class AppointmentForm(forms.ModelForm):
    specialty = forms.ModelChoiceField(queryset=MedicalSpecialty.objects.all(), required=True)

    class Meta:
        model = Appointment
        fields = ['specialty', 'date', 'time']  # scoatem 'clinic'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

