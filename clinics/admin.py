# # from django.contrib import admin
# # from .models import Clinic

# # admin.site.register(Clinic)

# from django.contrib import admin
# from .models import Clinic

# @admin.register(Clinic)
# class ClinicAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'city', 'address')
#     search_fields = ('name', 'email', 'city')
#     readonly_fields = ('password',)  # doar dacă nu vrei să fie modificată manual

#     fieldsets = (
#         (None, {
#             'fields': ('name', 'email', 'password', 'address', 'city', 'specialties')
#         }),
#     )
from django.contrib import admin
from .models import Clinic
from django import forms
from django.contrib.auth.hashers import make_password

class ClinicAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Clinic
        fields = '__all__'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return make_password(password)
        return self.instance.password  # returnăm parola existentă dacă nu s-a modificat

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    form = ClinicAdminForm
    list_display = ('name', 'email', 'city')
    search_fields = ('name', 'email', 'city')
