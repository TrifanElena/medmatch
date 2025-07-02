

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from reviews.models import Review
from clinics.models import Clinic

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
                return redirect('services:symptom_checker') 
            else:
                form.add_error(None, 'Email sau parolă incorecte.')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})



def choose(request):
    return render(request, 'users/choose.html')

def logout_user(request):
    logout(request)
    return redirect('users:login')

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'users/clinic_list.html', {'clinics': clinics})

@login_required
def reviews_list(request):
    qs = Review.objects.select_related(
        'appointment__clinic',
        'appointment__specialty',
        'appointment__patient'
    ).order_by('-created_at')

    clinic_id = request.GET.get('clinic_id')
    if clinic_id:
        qs = qs.filter(appointment__clinic_id=clinic_id)

    back_url = request.META.get('HTTP_REFERER', '/')
    return render(request, 'reviews/reviews_list.html', {
        'reviews': qs,
        'back_url': back_url
    })