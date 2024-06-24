from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Employee, HRManager, OnboardingTask, Document, TrainingModule, ITSupport, Notification

def request_onboarding(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        position = data.get('position')
        # Assume the user is already authenticated
        employee = Employee.objects.create(user=request.user, position=position)
        return JsonResponse({"message": "Onboarding requested"})

def assign_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        description = data.get('description')
        employee_id = data.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)
        OnboardingTask.objects.create(description=description, status='Pending', employee=employee)
        return JsonResponse({"message": "Task assigned successfully"})

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
        data = json.loads(request.body)
        employee_id = data.get('employee_id')
        resource_type = data.get('resource_type')
        employee = get_object_or_404(Employee, id=employee_id)
        ITSupport.objects.create(resource_type=resource_type, status='Setup', employee=employee)
        return JsonResponse({"message": "IT resources set up"})

def send_notification(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        recipient = data.get('recipient')
        Notification.objects.create(message=message, recipient=recipient)
        return JsonResponse({"message": "Notification sent"})

def employee_list(request):
    employees = Employee.objects.all().values('id', 'name')
    return JsonResponse(list(employees), safe=False)
