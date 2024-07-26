from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, JournalEntry
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        password = data.get('password')
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@csrf_exempt
def journal_entries(request):
    if request.method == 'GET':
        entries = JournalEntry.objects.all()
        data = [{'id': entry.id, 'date': entry.date, 'content': entry.content} for entry in entries]
        return JsonResponse({'entries': data})

    elif request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content')
        entry = JournalEntry.objects.create(student=request.user.student, content=content)
        return JsonResponse({'success': True, 'entry': {'id': entry.id, 'date': entry.date, 'content': entry.content}})

@csrf_exempt
def evaluate_student(request, student_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        evaluation = data.get('evaluation')
        try:
            student = Student.objects.get(id=student_id)
            student.journalentry_set.update(mentor_feedback=evaluation)
            return JsonResponse({'success': True})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Student not found'})
