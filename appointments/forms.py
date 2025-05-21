# # from django import forms
# # from .models import Appointment
# # from django.core.exceptions import ValidationError
# # from services.models import MedicalSpecialty
# # class AppointmentForm(forms.ModelForm):
# #     specialty = forms.ModelChoiceField(queryset=MedicalSpecialty.objects.all(), required=True)

# #     class Meta:
# #         model = Appointment
# #         fields = ['specialty', 'date', 'time']  # scoatem 'clinic'
# #         widgets = {
# #             'date': forms.DateInput(attrs={'type': 'date'}),
# #             'time': forms.TimeInput(attrs={'type': 'time'}),
# #         }

# from django.core.exceptions import ValidationError
# from .models import Appointment
# from services.models import MedicalSpecialty
# from django import forms
# from django.utils import timezone

# class AppointmentForm(forms.ModelForm):
#     specialty = forms.ModelChoiceField(queryset=MedicalSpecialty.objects.all(), required=True)

#     class Meta:
#         model = Appointment
#         fields = ['specialty', 'date', 'time']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'time': forms.TimeInput(attrs={'type': 'time'}),
#         }

#     def __init__(self, *args, **kwargs):
#         self.clinic = kwargs.pop('clinic', None)  # primim clinica din view
#         super().__init__(*args, **kwargs)

#     # def clean(self):
#     #     cleaned_data = super().clean()
#     #     specialty = cleaned_data.get('specialty')
#     #     date = cleaned_data.get('date')
#     #     time = cleaned_data.get('time')

#     #     if self.clinic and specialty and date and time:
#     #         conflict = Appointment.objects.filter(
#     #             clinic=self.clinic,
#     #             specialty=specialty,
#     #             date=date,
#     #             time=time
#     #         ).exists()
#     #         if conflict:
#     #             raise ValidationError("Există deja o programare la această clinică în acel interval.")
# def clean(self):
#     cleaned_data = super().clean()
#     specialty = cleaned_data.get('specialty')
#     date = cleaned_data.get('date')
#     time = cleaned_data.get('time')

#     # Nu permitem programări în trecut
#     if date and date < timezone.localdate():
#         raise ValidationError("Nu poți face o programare în trecut.")

#     if self.clinic and specialty and date and time:
#         conflict = Appointment.objects.filter(
#             clinic=self.clinic,
#             specialty=specialty,
#             date=date,
#             time=time
#         ).exists()
#         if conflict:
#             raise ValidationError("Există deja o programare la această clinică în acel interval.")

# from django.core.exceptions import ValidationError
# from .models import Appointment
# from services.models import MedicalSpecialty
# from django import forms
# from datetime import datetime

# class AppointmentForm(forms.ModelForm):
#     specialty = forms.ModelChoiceField(queryset=MedicalSpecialty.objects.all(), required=True)

#     class Meta:
#         model = Appointment
#         fields = ['specialty', 'date', 'time']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'time': forms.TimeInput(attrs={'type': 'time'}),
#         }

#     def __init__(self, *args, **kwargs):
#         self.clinic = kwargs.pop('clinic', None)
#         super().__init__(*args, **kwargs)

#     def clean(self):
#         cleaned_data = super().clean()
#         specialty = cleaned_data.get('specialty')
#         date_val = cleaned_data.get('date')
#         time_val = cleaned_data.get('time')

#         if not all([self.clinic, specialty, date_val, time_val]):
#             return

#         now = datetime.now()
#         selected_datetime = datetime.combine(date_val, time_val)

#         if selected_datetime < now:
#             raise ValidationError("Nu poți seta o programare în trecut.")

#         if Appointment.objects.filter(
#             clinic=self.clinic,
#             specialty=specialty,
#             date=date_val,
#             time=time_val
#         ).exists():
#             raise ValidationError("Există deja o programare la această clinică în acel interval.")
from django import forms
from django.core.exceptions import ValidationError
from .models import Appointment
from services.models import MedicalSpecialty
from datetime import date, datetime

class AppointmentForm(forms.ModelForm):
    specialty = forms.ModelChoiceField(queryset=MedicalSpecialty.objects.all(), required=True)

    class Meta:
        model = Appointment
        fields = ['specialty', 'date', 'time']
        widgets = {
            # 'date': forms.DateInput(attrs={'type': 'date'}),
            # 'time': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'specialty': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        self.clinic = kwargs.pop('clinic', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        specialty = cleaned_data.get('specialty')
        date_ = cleaned_data.get('date')
        time_ = cleaned_data.get('time')

        # Validare programare în trecut
        if date_ and time_:
            dt_combined = datetime.combine(date_, time_)
            if dt_combined < datetime.now():
                raise ValidationError("Nu poți face o programare în trecut.")

        # Validare programare duplicată
        if self.clinic and specialty and date_ and time_:
            exists = Appointment.objects.filter(
                clinic=self.clinic,
                specialty=specialty,
                date=date_,
                time=time_
            ).exists()
            if exists:
                raise ValidationError("Există deja o programare la această clinică în acel interval.")

        return cleaned_data
