from rest_framework import serializers
from .models import Mentor, Student, JournalEntry, Supervisor, Advice

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['id', 'name', 'email']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'internship_company', 'internship_start_date', 'internship_end_date']

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ['id', 'student', 'date', 'content', 'mentor_feedback', 'supervisor_feedback']

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['id', 'name', 'email']

class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = ['id', 'supervisor', 'student', 'advice', 'created_at']