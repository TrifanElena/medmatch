# from django import forms
# from users.models import User
# from .models import Patient


# class PatientRegistrationForm(forms.ModelForm):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = Patient
#         fields = ['full_name', 'city', 'phone_number']

#     def save(self, commit=True):
#         user = User.objects.create_user(
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password'],
#             is_patient=True
#         )
#         patient = super().save(commit=False)
#         patient.user = user
#         if commit:
#             patient.save()
#         return patient
# from django import forms
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class PatientRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email', 'full_name', 'city', 'phone_number', 'password']


# users/forms.py

# from django import forms
# from .models import User

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['full_name', 'email', 'password', 'city', 'phone_number']


#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         user.is_patient = True
#         if commit:
#             user.save()
#         return user


# users/forms.py

# from django import forms
# from .models import User

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['full_name', 'email', 'password', 'city', 'phone_number']
# users/forms.py
# from django import forms
# from .models import User

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email', 'full_name', 'city', 'phone_number', 'password']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         user.is_patient = True
#         if commit:
#             user.save()
#         return user
# from django import forms

# class UserLoginForm(forms.Form):
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label='Parolă', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# from django import forms
# from .models import User

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ['full_name', 'email', 'city', 'phone_number', 'password']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         user.is_patient = True  # Dacă vrei și pentru clinici, trebuie separat
#         if commit:
#             user.save()
#         return user


# class UserLoginForm(forms.Form):
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label='Parolă', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# users/forms.py
from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'city', 'phone_number', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_patient = True  # sau is_clinic=True, în funcție de înregistrare
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
