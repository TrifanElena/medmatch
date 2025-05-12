# clinics/urls.py
from django.urls import path
from . import views

app_name = 'clinics'

urlpatterns = [
    # Exemplu placeholder – modifică ulterior dacă ai view-uri
    path('', views.clinic_list, name='clinic_list'),
]
