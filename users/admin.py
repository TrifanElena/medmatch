from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'city', 'phone_number', 'is_patient', 'is_clinic')
    list_filter = ('is_patient', 'is_clinic', 'city')
    search_fields = ('email', 'full_name', 'city', 'phone_number')
