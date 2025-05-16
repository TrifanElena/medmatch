# clinics/urls.py
from django.urls import path
from . import views

app_name = 'clinics'

urlpatterns = [
    # Exemplu placeholder – modifică ulterior dacă ai view-uri
    
    path('register/', views.clinic_register, name='clinic_register'),
    path('login/', views.clinic_login, name='clinic_login'),
    path('dashboard/', views.clinic_dashboard, name='clinic_dashboard'),
    path('clinics_choose/', views.clinics_choose, name='clinics_choose'),
    
]
