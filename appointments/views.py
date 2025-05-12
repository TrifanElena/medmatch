from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

@login_required
def create_appointment(request):
    initial_data={}

    clinic_id=request.GET.get('clinic_id')
    if clinic_id:
        initial_data['clinic'] = clinic_id

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('services:home')  # sau o pagină de confirmare
    else:
        form = AppointmentForm(initial=initial_data)

    return render(request, 'appointments/create_appointment.html', {'form': form})
