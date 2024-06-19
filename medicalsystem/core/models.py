# core/models.py

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, default='N/A')  # Default value added
    email = models.EmailField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment on {self.date} at {self.time}"

class MedicalHistory(models.Model):
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"MedicalHistory on {self.date}"

class Payment(models.Model):
    date = models.DateField()
    amount = models.FloatField()
    status = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment of {self.amount} on {self.date}"
