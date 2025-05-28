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
            'specialties': forms.CheckboxSelectMultiple(attrs={
                'class': 'btn-check',
                'autocomplete': 'off',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add form-control to all text inputs
        text_fields = ['name', 'email', 'address', 'city']
        for f in text_fields:
            self.fields[f].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[f].label
            })
        # password field too
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Parolă'
        })    

    def save(self, commit=True):
        clinic = super().save(commit=False)
        clinic.set_password(self.cleaned_data['password'])
        if commit:
            clinic.save()
            self.save_m2m()
        return clinic
