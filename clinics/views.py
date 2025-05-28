# # clinics/views.py
# from django.shortcuts import render
# from .models import Clinic

# def clinic_list(request):
#     clinics = Clinic.objects.all()
#     return render(request, 'clinics/clinic_list.html', {'clinics': clinics})

# clinics/views.py
# from django.http import HttpResponse

# def clinic_list(request):
#     return HttpResponse("Listă de clinici disponibile.")
# from django.shortcuts import render, redirect
# from .forms import ClinicRegistrationForm
# from .models import Clinic

# def clinic_register(request):
#     if request.method == 'POST':
#         form = ClinicRegistrationForm(request.POST)
#         if form.is_valid():
#             clinic = form.save(commit=False)
#             clinic.set_password(form.cleaned_data['password'])
#             clinic.save()
#             form.save_m2m()
#             return redirect('clinics:login')
#     else:
#         form = ClinicRegistrationForm()
#     return render(request, 'clinics/register.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClinicRegistrationForm, ClinicLoginForm
from .models import Clinic
from datetime import date
from appointments.models import Appointment
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser


@require_POST
def delete_expired_appointment(request):
    clinic_id = request.session.get('clinic_id')
    if not clinic_id:
        messages.error(request, "Autentificare necesară.")
        return redirect('clinics:clinic_login')

    appointment_id = request.POST.get('appointment_id')
    appointment = get_object_or_404(Appointment, id=appointment_id, clinic_id=clinic_id)

    # Se poate șterge doar dacă e în trecut și neîndeplinită
    if appointment.date < timezone.now().date() and not appointment.fulfilled:
        appointment.delete()
        messages.success(request, "Programarea a fost ștearsă.")
    else:
        messages.error(request, "Programarea nu poate fi ștearsă.")

    return redirect('clinics:clinic_dashboard')

def clinic_register(request):
    if request.method == 'POST':
        form = ClinicRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Clinica a fost înregistrată cu succes! Acum vă puteți conecta.")
            return redirect('clinics:clinic_login')
    else:
        form = ClinicRegistrationForm()

    return render(request, 'clinics/clinic_register.html', {'form': form})


# def clinic_login(request):
#     form = ClinicLoginForm()
    
#     if request.method == 'POST':
#         form = ClinicLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             try:
#                 clinic = Clinic.objects.get(email=email)
#                 if clinic.check_password(password):
#                     request.session['clinic_id'] = clinic.id
#                     return redirect('clinics:clinic_dashboard')
#                 else:
#                     messages.error(request, 'Parola este incorectă.')
#             except Clinic.DoesNotExist:
#                 messages.error(request, 'Clinica nu există.')

#     return render(request, 'clinics/clinic_login.html', {'form': form})
def clinic_login(request):
    form = ClinicLoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        # 1) Try to find the clinic
        try:
            clinic = Clinic.objects.get(email=email)
        except Clinic.DoesNotExist:
            messages.error(request, "Clinica nu există.")
            # render same login page with error
            return render(request, 'clinics/clinic_login.html', {'form': form})

        # 2) Check password
        if not clinic.check_password(password):
            messages.error(request, "Parola este incorectă.")
            return render(request, 'clinics/clinic_login.html', {'form': form})

        # 3) Success! log them in via session and clear any old messages
        request.session['clinic_id'] = clinic.id
        list(messages.get_messages(request))   # drain old messages
        return redirect('clinics:clinic_dashboard')

    # GET or non-valid form
    return render(request, 'clinics/clinic_login.html', {'form': form})

def clinics_choose(request):
    return render(request, 'clinics/clinics_choose.html')

def clinic_dashboard(request):
    clinic_id = request.session.get('clinic_id')
    if not clinic_id:
        messages.error(request, "Trebuie să te autentifici.")
        return redirect('clinics:clinic_login')

    clinic = get_object_or_404(Clinic, id=clinic_id)
    appointments = Appointment.objects.filter(clinic=clinic).select_related('patient')

    if request.method == 'POST':
        if 'appointment_id' in request.POST:
            appointment_id = request.POST.get('appointment_id')
            fulfilled = request.POST.get('fulfilled') == 'on'
            # appointment = Appointment.objects.get(id=appointment_id)
            appointment = get_object_or_404(Appointment, id=appointment_id)
            appointment.fulfilled = fulfilled
            appointment.save()
            messages.success(request, "Statusul programării a fost actualizat.")
            return redirect('clinics:clinic_dashboard')
    
    if 'delete_appointment_id' in request.POST:
            appointment_id = request.POST.get('delete_appointment_id')
            appointment = get_object_or_404(Appointment, id=appointment_id)
            appointment.delete()
            messages.success(request, "Programarea a fost ștearsă.")
            return redirect('clinics:clinic_dashboard')


    return render(request, 'clinics/clinic_dashboard.html', {
        'clinic': clinic,
        'appointments': appointments,
        # 'today': date.today(),
        'today': timezone.localdate(),
    })

