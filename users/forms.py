#
# users/forms.py
# from django import forms
# from .models import User
# from django.contrib.auth.forms import AuthenticationForm

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email', 'full_name', 'city', 'phone_number', 'password']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         user.is_patient = True  # sau is_clinic=True, în funcție de înregistrare
#         if commit:
#             user.save()
#         return user


# class UserLoginForm(forms.Form):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from clinics.models import Clinic

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Extragem orașele distincte din clinici pentru dropdown
        clinic_cities = Clinic.objects.values_list('city', flat=True).distinct()
        city_choices = [(city, city) for city in clinic_cities]
        self.fields['city'] = forms.ChoiceField(
            choices=city_choices,
            label='Oraș',
            required=True
        )

    class Meta:
        model = User
        fields = ['email', 'full_name', 'city', 'phone_number', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_patient = True
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
