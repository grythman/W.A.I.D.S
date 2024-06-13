from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Employee, HRManager, OnboardingTask, Document, TrainingModule, ITSupport, Notification

def home(request):
    return render(request, 'onboarding/home.html')

def request_onboarding(request):
    if request.method == 'POST':
        # Assuming the user is authenticated and is an employee
        user = request.user
        employee = Employee.objects.create(user=user, position=request.POST.get('position'))
        # Add default onboarding tasks, documents, etc.
        OnboardingTask.objects.create(description='Complete HR Forms', status='Pending', employee=employee)
        Document.objects.create(type='ID Proof', status='Pending', employee=employee)
        TrainingModule.objects.create(title='Orientation', description='Introduction to the company', status='Pending', employee=employee)
        ITSupport.objects.create(resource_type='Laptop', status='Pending', employee=employee)
        
        return JsonResponse({"message": "Onboarding requested", "employee_id": employee.id})

def assign_task(request):
    if request.method == 'POST':
        task_description = request.POST.get('description')
        employee_id = request.POST.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)
        task = OnboardingTask.objects.create(description=task_description, status='Pending', employee=employee)
        
        return JsonResponse({"message": "Task assigned", "task_id": task.id})

def complete_task(request, task_id):
    task = get_object_or_404(OnboardingTask, id=task_id)
    task.status = "Completed"
    task.save()
    return JsonResponse({"message": "Task completed"})

def submit_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.status = "Submitted"
    document.save()
    return JsonResponse({"message": "Document submitted"})

def complete_module(request, module_id):
    module = get_object_or_404(TrainingModule, id=module_id)
    module.status = "Completed"
    module.save()
    return JsonResponse({"message": "Module completed"})

def setup_it_resources(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        resource_type = request.POST.get('resource_type')
        employee = get_object_or_404(Employee, id=employee_id)
        it_support = ITSupport.objects.create(resource_type=resource_type, status='Pending', employee=employee)
        return JsonResponse({"message": "IT resources setup", "it_support_id": it_support.id})

def send_notification(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        recipient_email = request.POST.get('recipient')
        notification = Notification.objects.create(message=message, recipient=recipient_email)
        # You would normally send an email here
        return JsonResponse({"message": "Notification sent", "notification_id": notification.id})
