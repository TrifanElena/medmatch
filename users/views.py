# from django.shortcuts import render, redirect
# from .forms import PatientRegistrationForm

# def register_patient(request):
#     if request.method == 'POST':
#         form = PatientRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # sau o pagină de confirmare
#     else:
#         form = PatientRegistrationForm()
#     return render(request, 'patients/register.html', {'form': form})

# from django.shortcuts import render, redirect
# from .forms import PatientRegistrationForm
# from django.contrib.auth import login
# from django.contrib.auth import get_user_model

# User = get_user_model()

# def register_patient(request):
#     if request.method == 'POST':
#         form = PatientRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_patient = True
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect('services:symptom_checker')
#     else:
#         form = PatientRegistrationForm()
#     return render(request, 'users/register_patient.html', {'form': form})

# users/views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from .forms import UserRegistrationForm
# from .models import User

# def register_patient(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_patient = True
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect('home')  # redirecționează unde vrei tu
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'users/register.html', {'form': form})


# users/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from .forms import UserRegistrationForm
# from django.contrib import messages


# def register_user(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # sau unde vrei tu
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'users/register.html', {'form': form})
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib import messages

# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')  # sau altă pagină principală
#         else:
#             messages.error(request, 'Email sau parolă incorecte.')
#     return render(request, 'users/login.html')

# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from .forms import UserLoginForm

# def login_user(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('services:symptom_checker')
#             else:
#                 form.add_error(None, 'Email sau parolă incorecte.')
#     else:
#         form = UserLoginForm()

#     return render(request, 'users/login.html', {'form': form})

# # users/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from .forms import UserRegistrationForm, UserLoginForm
# from .models import User
# from django.contrib import messages

# def register_user(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('services:symptom_checker')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'users/register.html', {'form': form})


# def login_user(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('services:symptom_checker')
#             else:
#                 form.add_error(None, 'Email sau parolă incorecte.')
#     else:
#         form = UserLoginForm()

#     return render(request, 'users/login.html', {'form': form})
   

# def choose_user_type(request):
#     return render(request, 'users/choose.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('services:symptom_checker')  # după înregistrare
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('services:symptom_checker')  # după login
            else:
                form.add_error(None, 'Email sau parolă incorecte.')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def choose_user_type(request):
    return render(request, 'users/choose.html')

def logout_user(request):
    logout(request)
    return redirect('users:login')