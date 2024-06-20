# core/admin.py

from django.contrib import admin
from .models import Patient, Doctor, Appointment, MedicalHistory, Payment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(MedicalHistory)
admin.site.register(Payment)
