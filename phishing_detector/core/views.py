from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import Email, URL, Report, PhishingDetector
from .forms import EmailForm, URLForm, LoginForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})


def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})


def check_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save()
            is_phishing = PhishingDetector.analyzeEmail(email)
            report = Report.generateReport(request.user, f'Email analysis result: {is_phishing}')
            return redirect('report', report_id=report.id)
    else:
        form = EmailForm()
    return render(request, 'core/check_email.html', {'form': form})

def check_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            is_phishing = PhishingDetector.analyzeURL(url)
            report = Report.generateReport(request.user, f'URL analysis result: {is_phishing}')
            return redirect('report', report_id=report.id)
    else:
        form = URLForm()
    return render(request, 'core/check_url.html', {'form': form})

def report(request, report_id):
    report = Report.objects.get(id=report_id)
    return render(request, 'core/report.html', {'report': report})
