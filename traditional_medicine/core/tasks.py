# tasks.py
from celery import shared_task
from .models import Appointment

@shared_task
def send_reminder_email(appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    # Send reminder email logic here
