from django.contrib import admin
from .models import Patient, Doctor, Appointment, Payment, MedicalHistory

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(MedicalHistory)
