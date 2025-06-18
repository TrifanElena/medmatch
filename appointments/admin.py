# appointments/admin.py
import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display   = ('clinic', 'specialty', 'date', 'time', 'fulfilled')
    list_filter    = ('fulfilled', 'date')
    date_hierarchy = 'date'
    actions        = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        """
        Exportă obiectele selectate ca CSV cu coloanele: date, fulfilled
        """
        meta = self.model._meta
        field_names = ['date', 'fulfilled']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=appointments.csv'
        writer = csv.writer(response)

        # header
        writer.writerow(field_names)
        # date rows
        for obj in queryset:
            row = [getattr(obj, field) for field in field_names]
            writer.writerow(row)

        return response

    export_as_csv.short_description = "Exportă ca CSV (date, fulfilled)"
