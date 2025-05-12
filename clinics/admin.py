# from django.contrib import admin
# from .models import Clinic

# admin.site.register(Clinic)

from django.contrib import admin
from .models import Clinic

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address')
