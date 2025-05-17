"""
URL configuration for medical_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# medical_platform/urls.py


# from django.contrib import admin
# from django.urls import path, include
# from services import views as service_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#       path('accounts/', include('django.contrib.auth.urls')),
#     path('api/users/', include('users.urls')),
#     path('services/', include('services.urls', namespace='services')),  # păstrează symptoms etc.
#     path('', service_views.home, name='home'),

# ]

# medical_platform/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('clinics/', include('clinics.urls', namespace='clinics')),
#     path('', include('services.urls')),  # sau alt app principal
# ]

# from django.contrib import admin
# from django.urls import path, include
# from services import views as service_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('services/', include(('services.urls', 'services'), namespace='services')),
#     path('clinics/', include(('clinics.urls', 'clinics'), namespace='clinics')),
#     path('users/', include(('users.urls', 'users'), namespace='users')),
#     path('', service_views.home, name='home'),
# ]

# medical_platform/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('users.urls')),  # Fără namespace aici, doar include simplu
#     path('services/', include('services.urls')),
#     path('clinics/', include('clinics.urls')),
# ]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('users.urls', namespace='users')),
#     path('services/', include('services.urls', namespace='services')),
#     path('clinics/', include('clinics.urls', namespace='clinics')),

#     # trimite path-ul gol către homepage-ul din services
#     path('', include('services.urls', namespace='services')),
# ]

from django.contrib import admin
from django.urls import path, include
from services import views as service_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include(('services.urls', 'services'), namespace='services')),
    path('clinics/', include(('clinics.urls', 'clinics'), namespace='clinics')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('appointments/', include(('appointments.urls', 'appointments'), namespace='appointments')),
    path('reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),
    path('', service_views.home, name='home'),  
]

