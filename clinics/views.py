# # clinics/views.py
# from django.shortcuts import render
# from .models import Clinic

# def clinic_list(request):
#     clinics = Clinic.objects.all()
#     return render(request, 'clinics/clinic_list.html', {'clinics': clinics})

# clinics/views.py
from django.http import HttpResponse

def clinic_list(request):
    return HttpResponse("Listă de clinici disponibile.")
