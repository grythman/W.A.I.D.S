# api/models.py

from django.db import models
from datetime import date

class Patient(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(default=date.today) 
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=255, default="N/A")
    address = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, default="N/A") 
    email = models.EmailField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.CharField(max_length=255, default="General Consultation")  # Default value added
    notes = models.TextField(default="No notes")  # Default value added

    def __str__(self):
        return f"{self.patient.name} with {self.doctor.name} on {self.date}"

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.patient.name} on {self.date}"

class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.patient.name} - {self.amount} on {self.date}"
