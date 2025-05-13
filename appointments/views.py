# from django.shortcuts import render, redirect
# from .forms import AppointmentForm
# from django.contrib.auth.decorators import login_required

# @login_required
# def create_appointment(request):
#     initial_data={}

#     clinic_id=request.GET.get('clinic_id')
#     if clinic_id:
#         initial_data['clinic'] = clinic_id

#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.patient = request.user
#             appointment.save()
#             return redirect('services:home')  # sau o pagină de confirmare
#     else:
#         form = AppointmentForm(initial=initial_data)

#     return render(request, 'appointments/create_appointment.html', {'form': form})

# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import AppointmentForm
# from clinics.models import Clinic
# from services.models import MedicalSpecialty
# from .models import Appointment
# from django.contrib.auth.decorators import login_required

# @login_required
# def create_appointment(request):
#     clinic_id = request.GET.get('clinic_id')
#     specialty_id = request.GET.get('specialty_id')  # poate fi transmis din URL

#     clinic = get_object_or_404(Clinic, id=clinic_id)
#     recommended_specialty = None

#     if specialty_id:
#         recommended_specialty = get_object_or_404(MedicalSpecialty, id=specialty_id)
#     elif clinic.specialties.exists():
#         recommended_specialty = clinic.specialties.first()  # fallback

#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.patient = request.user
#             appointment.clinic = clinic
#             appointment.specialty = recommended_specialty
#             appointment.save()
#             return redirect('appointments:confirmation', appointment_id=appointment.id)
#     else:
#         form = AppointmentForm()

#     return render(request, 'appointments/create_appointment.html', {
#         'form': form,
#         'clinic': clinic,
#         'recommended_specialty': recommended_specialty,
#     })

# def appointment_confirmation(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id)
#     clinic = appointment.clinic
#     specialty = appointment.specialty.name if appointment.specialty else "Nespecificată"
    
#     context = {
#         'appointment': appointment,
#         'clinic': clinic,
#         'specialty': specialty,
#         'clinic_email': getattr(clinic, 'email', 'Nu este disponibil')
#     }
#     return render(request, 'appointments/confirmation.html', context)
# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import AppointmentForm
# from clinics.models import Clinic
# from services.models import MedicalSpecialty
# from .models import Appointment
# from django.contrib.auth.decorators import login_required

# @login_required
# def create_appointment(request):
#     clinic_id = request.GET.get('clinic_id')
#     specialty_id = request.GET.get('specialty_id')

#     clinic = get_object_or_404(Clinic, id=clinic_id)
#     recommended_specialty = None

#     if specialty_id:
#         recommended_specialty = get_object_or_404(MedicalSpecialty, id=specialty_id)
#         if recommended_specialty not in clinic.specialties.all():
#             recommended_specialty = clinic.specialties.first()
#     else:
#         recommended_specialty = clinic.specialties.first()

#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.patient = request.user
#             appointment.clinic = clinic
#             appointment.specialty = recommended_specialty
#             appointment.save()
#             return redirect('appointments:confirmation', appointment_id=appointment.id)
#     else:
#         form = AppointmentForm()

#     return render(request, 'appointments/create_appointment.html', {
#         'form': form,
#         'clinic': clinic,
#         'recommended_specialty': recommended_specialty,
#     })

# def appointment_confirmation(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id)
#     clinic = appointment.clinic
#     specialty = appointment.specialty.name if appointment.specialty else "Nespecificată"

#     context = {
#         'appointment': appointment,
#         'clinic': clinic,
#         'specialty': specialty,
#         'clinic_email': getattr(clinic, 'email', 'Nu este disponibil')
#     }
#     return render(request, 'appointments/confirmation.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from clinics.models import Clinic
from services.models import MedicalSpecialty
from .models import Appointment
from django.contrib.auth.decorators import login_required

@login_required
def create_appointment(request):
    clinic_id = request.GET.get('clinic_id')
    specialty_id = request.GET.get('specialty_id')

    clinic = get_object_or_404(Clinic, id=clinic_id)
    recommended_specialty = None

    if specialty_id:
        try:
            recommended_specialty = MedicalSpecialty.objects.get(id=specialty_id)
        except MedicalSpecialty.DoesNotExist:
            recommended_specialty = None

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        form.fields['specialty'].queryset = clinic.specialties.all()  # important
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.clinic = clinic
            appointment.specialty = form.cleaned_data['specialty']
            appointment.save()
            return redirect('appointments:confirmation', appointment_id=appointment.id)
        else:
            print("❌ Formular INVALID:", form.errors)
    else:
        form = AppointmentForm()
        form.fields['specialty'].queryset = clinic.specialties.all()
        if recommended_specialty:
            form.initial['specialty'] = recommended_specialty

    return render(request, 'appointments/create_appointment.html', {
        'form': form,
        'clinic': clinic,
        'recommended_specialty': recommended_specialty,
    })

@login_required
def appointment_confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointments/confirmation.html', {
        'appointment': appointment,
        'clinic': appointment.clinic,
        'specialty': appointment.specialty.name if appointment.specialty else "Nespecificată",
        'clinic_email': appointment.clinic.email if hasattr(appointment.clinic, 'email') else 'Email indisponibil',
    })
