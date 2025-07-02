#appointments/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_reminder_email(appointment):
    subject = "Reminder: Programarea ta la clinică este mâine"
    message = f"""
Bună {appointment.patient.full_name},

Îți reamintim că ai o programare la clinica {appointment.clinic.name}, specialitatea {appointment.specialty.name}, pe data de {appointment.date} la ora {appointment.time}.

Adresă: {appointment.clinic.address}

Multă sănătate!
Echipa MedMatch
    """
    recipient = appointment.patient.email
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
 