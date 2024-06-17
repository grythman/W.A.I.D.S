from django import forms
from .models import Patient, Doctor, Appointment, Payment, MedicalRecord

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['user', 'phone', 'address', 'medical_history', 'date_of_birth', 'emergency_contact']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['user', 'specialty', 'phone']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'reason']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['patient', 'amount', 'payment_date', 'payment_method']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'diagnosis', 'prescription', 'visit_date']
