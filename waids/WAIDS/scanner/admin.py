# scanner/admin.py
from django.contrib import admin
from .models import Vulnerability, ScanReport, Attack

admin.site.register(Vulnerability)
admin.site.register(ScanReport)
admin.site.register(Attack)

