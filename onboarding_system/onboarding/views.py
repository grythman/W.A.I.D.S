from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Employee, OnboardingTask, Document, TrainingModule, ITSupport, Notification

def home(request):
    return render(request, 'onboarding/index.html')

def request_onboarding(request):
    # Handle onboarding request
    return JsonResponse({"message": "Onboarding requested"})

def assign_task(request):
    # Handle task assignment
    return JsonResponse({"message": "Task assigned"})

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
    # Handle IT resource setup
    return JsonResponse({"message": "IT resources set up"})

def send_notification(request):
    # Handle sending notification
    return JsonResponse({"message": "Notification sent"})
