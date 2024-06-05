# scanner/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import ScanReport, Vulnerability, Attack

def index(request):
    return render(request, 'scanner/index.html')

def scan_report(request):
    reports = ScanReport.objects.all()
    return render(request, 'scanner/scan_report.html', {'reports': reports})

def attack_list(request):
    attacks = Attack.objects.all()
    return render(request, 'scanner/attack_list.html', {'attacks': attacks})
