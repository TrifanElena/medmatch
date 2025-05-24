# reviews/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from .models import Clinic
from clinics.models import Clinic
from appointments.models import Appointment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# @login_required
# def leave_review(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

#     if not appointment.fulfilled:
#         messages.error(request, "Această programare nu este eligibilă pentru recenzie.")
#         return render(request, 'reviews/leave_review.html', {'appointment': appointment})


#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.appointment = appointment
#             review.save()
#             messages.success(request, "Mulțumim pentru recenzie! Sperăm că serviciile noastre medicale s-au aliniat nevoilor dumneavoastră.")
#             return redirect('appointments:my_appointments')
#     else:
#         form = ReviewForm()

#     return render(request, 'reviews/leave_review.html', {
#         'form': form,
#         'appointment': appointment
#     })
@login_required
def leave_review(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

    if not appointment.fulfilled:
        messages.error(request, "Această programare nu este eligibilă pentru recenzie.")
        return render(request, 'reviews/leave_review.html', {'appointment': appointment})

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.appointment = appointment
            review.save()
            messages.success(request, "Felicitări! Recenzia a fost trimisă! Sperăm că serviciile noastre medicale au fost pe măsura așteptărilor dumneavoastră.")
            return render(request, 'reviews/leave_review.html', {
                'form': ReviewForm(),  # formular gol
                'appointment': appointment
            })
    else:
        form = ReviewForm()

    return render(request, 'reviews/leave_review.html', {
        'form': form,
        'appointment': appointment
    })


# def reviews_list(request):
#     reviews = Review.objects.select_related('appointment__clinic', 'appointment__specialty', 'appointment__patient').all().order_by('-created_at')
#     return render(request, 'reviews/reviews_list.html', {'reviews': reviews})

# def reviews_list(request):
#     reviews = Review.objects.select_related('appointment__clinic', 'appointment__specialty', 'appointment__patient').all().order_by('-created_at')
    
#     previous_url = request.META.get('HTTP_REFERER', '/services/symptoms/')  # fallback: symptom_checker

#     return render(request, 'reviews/reviews_list.html', {
#         'reviews': reviews,
#         'back_url': previous_url
#     })

@login_required
def reviews_list(request):
    clinic_id = request.GET.get('clinic_id')
    # preluăm toate recenziile, împreună cu relațiile necesare
    reviews = Review.objects.select_related(
    # qs = Review.objects.select_related(
        'appointment__clinic',
        'appointment__specialty',
        'appointment__patient'
    ).order_by('-created_at')

    context = {'reviews': reviews}
    # dacă a fost dat clinic_id în URL, filtrăm
    # if clinic_id:
    #     qs = qs.filter(appointment__clinic_id=clinic_id)

    # back_url = request.META.get('HTTP_REFERER', '/services/symptoms/')

    # return render(
    #     request,
    #     'reviews/reviews_list.html',
    #     {
    #         'reviews': qs,
    #         'back_url': back_url
    #     }
    # )
    if clinic_id:
        # validare că există clinica
        clinic = get_object_or_404(Clinic, id=clinic_id)
        reviews = reviews.filter(appointment__clinic=clinic)
        context.update({
            'reviews': reviews,
            'current_clinic': clinic
        })

    # url-ul anterior
    context['back_url'] = request.META.get('HTTP_REFERER', '/services/symptoms/')

    return render(request, 'reviews/reviews_list.html', context)

def clinic_list(request):
    # prefetchăm specializările pentru performanță
    clinics = Clinic.objects.prefetch_related('specialties').all()
    return render(request, 'clinics/clinic_list.html', {
        'clinics': clinics
    })