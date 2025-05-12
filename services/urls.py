# services/urls.py

from django.urls import path, include
from . import views

app_name = 'services'  # definim namespace-ul

urlpatterns = [
    path('symptoms/', views.symptom_checker, name='symptom_checker'),
    path('recommendation/', views.recommend_specialty, name='recommend_specialty'),
     path('', views.home, name='home'),
    # `path('patients/', include('users.urls')),`

]
