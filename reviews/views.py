# reviews/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from appointments.models import Appointment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def leave_review(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

    # doar dacă e îndeplinită și nu are deja review
    # if not appointment.fulfilled or hasattr(appointment, 'review'):
    #     messages.error(request, "Această programare nu este eligibilă pentru recenzie.")
    #     return redirect('appointments:my_appointments')
    if not appointment.fulfilled:
        messages.error(request, "Această programare nu este eligibilă pentru recenzie.")
        return render(request, 'reviews/leave_review.html', {'appointment': appointment})


    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.appointment = appointment
            review.save()
            messages.success(request, "Mulțumim pentru recenzie! Sperăm că serviciile noastre medicale s-au aliniat nevoilor dumneavoastră.")
            return redirect('appointments:my_appointments')
    else:
        form = ReviewForm()

    return render(request, 'reviews/leave_review.html', {
        'form': form,
        'appointment': appointment
    })

def reviews_list(request):
    reviews = Review.objects.select_related('appointment__clinic', 'appointment__specialty', 'appointment__patient').all().order_by('-created_at')
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews})