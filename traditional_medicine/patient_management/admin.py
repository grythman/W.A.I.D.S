from django.contrib import admin
from .models import Patient, Doctor, Appointment, Payment, MedicalRecord

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(MedicalRecord)
