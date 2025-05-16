from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from clinics.models import Clinic
from services.models import MedicalSpecialty
from .models import Appointment
from django.contrib.auth.decorators import login_required

# @login_required
# def create_appointment(request):
#     clinic_id = request.GET.get('clinic_id')
#     specialty_id = request.GET.get('specialty_id')

#     clinic = get_object_or_404(Clinic, id=clinic_id)
#     recommended_specialty = None

#     if specialty_id:
#         try:
#             recommended_specialty = MedicalSpecialty.objects.get(id=specialty_id)
#         except MedicalSpecialty.DoesNotExist:
#             recommended_specialty = None

#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         form.fields['specialty'].queryset = clinic.specialties.all()  # important
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.patient = request.user
#             appointment.clinic = clinic
#             appointment.specialty = form.cleaned_data['specialty']
#             appointment.save()
#             return redirect('appointments:confirmation', appointment_id=appointment.id)
#         else:
#             print("❌ Formular INVALID:", form.errors)
#     else:
#         form = AppointmentForm()
#         form.fields['specialty'].queryset = clinic.specialties.all()
#         if recommended_specialty:
#             form.initial['specialty'] = recommended_specialty

#     return render(request, 'appointments/create_appointment.html', {
#         'form': form,
#         'clinic': clinic,
#         'recommended_specialty': recommended_specialty,
#     })
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
        # trimitem clinica către formular
        form = AppointmentForm(request.POST, clinic=clinic)
        form.fields['specialty'].queryset = clinic.specialties.all()

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
        form = AppointmentForm(clinic=clinic)
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
    diagnosis = request.session.get( 'diagnosis')
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointments/confirmation.html', {
        'appointment': appointment,
        'clinic': appointment.clinic,
        'specialty': appointment.specialty.name if appointment.specialty else "Nespecificată",
        'clinic_email': appointment.clinic.email if hasattr(appointment.clinic, 'email') else 'Email indisponibil',
        'diagnosis': diagnosis
    })
