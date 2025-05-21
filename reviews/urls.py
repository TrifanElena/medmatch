# reviews/urls.py
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('leave/<int:appointment_id>/', views.leave_review, name='leave_review'),
    path(' ', views.reviews_list, name='list'),
    path('', views.reviews_list, name='reviews_list'),
]
