# reviews/urls.py
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('leave/<int:appointment_id>/', views.leave_review, name='leave_review'),
    path('all/', views.reviews_list, name='list'),
]
