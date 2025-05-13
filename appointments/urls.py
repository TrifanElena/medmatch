from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('create/', views.create_appointment, name='create'),
    path('confirmation/<int:appointment_id>/', views.appointment_confirmation, name='confirmation'),

]