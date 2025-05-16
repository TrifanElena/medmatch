# from django import forms
# from .models import Clinic
# from services.models import MedicalSpecialty

# class ClinicRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = Clinic
#         fields = ['name', 'email', 'password', 'address', 'city', 'specialties']
#         widgets = {
#             'specialties': forms.CheckboxSelectMultiple
#         }
from django import forms
from .models import Clinic
from services.models import MedicalSpecialty

class ClinicLoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Parolă", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ClinicRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Clinic
        fields = ['name', 'email', 'password', 'address', 'city', 'specialties']
        widgets = {
            'specialties': forms.CheckboxSelectMultiple
        }

    def save(self, commit=True):
        clinic = super().save(commit=False)
        clinic.set_password(self.cleaned_data['password'])
        if commit:
            clinic.save()
            self.save_m2m()
        return clinic
