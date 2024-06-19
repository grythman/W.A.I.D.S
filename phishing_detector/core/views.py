from django.shortcuts import render, redirect
from .models import Email, URL, Report
from .forms import EmailForm, URLForm, RegistrationForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'core/home.html')

def login_user(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        # Successful login (implementation depends on your authentication framework)
        login(request, user)  # Assuming you're using Django's built-in login function
        return True
    else:
        # Invalid credentials
        return False

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the new user to the database
            # Optionally, handle successful registration (e.g., redirect to login page)
            return redirect('login')  # Assuming you have a login URL pattern
    else:
        form = RegistrationForm()

    return render(request, 'core/register.html', {'form': form})


def check_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.is_phishing = detect_phishing(email.content)
            email.save()
            return redirect('report', report_id=email.id)
    else:
        form = EmailForm()
    return render(request, 'core/check_email.html', {'form': form})

def check_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.is_phishing = detect_phishing(url.link)
            url.save()
            return redirect('report', report_id=url.id)
    else:
        form = URLForm()
    return render(request, 'core/check_url.html', {'form': form})

def report(request, report_id):
    report = Report.objects.get(id=report_id)
    return render(request, 'core/report.html', {'report': report})

def detect_phishing(content):
    # Here you will use your phishing detection logic.
    # For now, let's assume it always returns False.
    return False
