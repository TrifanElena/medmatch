# from django.contrib import admin
# from .models import User

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'full_name', 'city', 'phone_number', 'is_patient', 'is_clinic')
#     list_filter = ('is_patient', 'is_clinic', 'city')
#     search_fields = ('email', 'full_name', 'city', 'phone_number')
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     list_display = ('email', 'full_name', 'city', 'phone_number', 'is_patient', 'is_clinic', 'is_staff')
#     list_filter = ('is_patient', 'is_clinic', 'city')
#     search_fields = ('email', 'full_name', 'city', 'phone_number')
#     ordering = ('email',)

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Date personale', {'fields': ('full_name', 'city', 'phone_number')}),
#         ('Permisiuni', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Roluri', {'fields': ('is_patient', 'is_clinic')}),
#         ('Date importante', {'fields': ('last_login',)}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2',
#                        'full_name', 'city', 'phone_number',
#                        'is_patient', 'is_clinic')
#         }),
#     )

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .admin_forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('email', 'full_name', 'city', 'phone_number', 'is_patient', 'is_clinic', 'is_staff')
    list_filter = ('is_patient', 'is_clinic', 'city')
    search_fields = ('email', 'full_name', 'city', 'phone_number')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informații personale', {'fields': ('full_name', 'city', 'phone_number')}),
        ('Permisiuni', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Roluri', {'fields': ('is_patient', 'is_clinic')}),
        ('Date importante', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',
                       'full_name', 'city', 'phone_number',
                       'is_patient', 'is_clinic', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )
