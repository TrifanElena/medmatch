# # 
# from django.urls import path
# from . import views

# app_name = 'users'

# urlpatterns = [
#     path('register/', views.register_patient, name='register'),
# ]


# from django.urls import path
# from . import views
# from django.contrib.auth.views import LogoutView

# app_name = 'users'

# urlpatterns = [
#     path('register/', views.register_user, name='register'),
#     path('login/', views.login_user, name='login'),
#      path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
#      path('choose/', views.choose_auth, name='choose_auth'),
#     # etc.
# ]

# users/urls.py
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),  # <- schimbă 'login' în 'login_user'
    path('logout/', views.logout_user, name='logout'),
    path('', views.clinic_list, name='clinic_list'),
    path('choose/', views.choose, name='choose'),  # opțional, dacă ai pagină de alegere tip
]
