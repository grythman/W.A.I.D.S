# scanner/models.py
from django.db import models
from django.contrib.auth.models import User

class Vulnerability(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    severity = models.CharField(max_length=50)

class ScanReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    vulnerabilities = models.ManyToManyField(Vulnerability)

class Attack(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()
    detected_date = models.DateTimeField(auto_now_add=True)
