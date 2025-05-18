from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from appointments.models import Appointment
from appointments.utils import send_reminder_email

class Command(BaseCommand):
    help = 'Trimite remindere cu o zi înainte de programare'

    def handle(self, *args, **kwargs):
        tomorrow = timezone.localdate() + timedelta(days=1)
        appointments = Appointment.objects.filter(date=tomorrow, fulfilled=False)

        for appointment in appointments:
            send_reminder_email(appointment)
            self.stdout.write(f"Reminder trimis pentru programarea {appointment.id}")
