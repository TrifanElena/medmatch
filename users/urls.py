
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),  
    path('logout/', views.logout_user, name='logout'),
    path('clinics/', views.clinic_list, name='clinic_list'),
    path('choose/', views.choose, name='choose'),  
]
