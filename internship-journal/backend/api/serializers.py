from rest_framework import serializers
from .models import Mentor, Student, JournalEntry, Supervisor, Advice

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['id', 'name', 'email']

class JournalEntrySerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    mentor_feedback = serializers.CharField(required=False, allow_blank=True)
    supervisor_feedback = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = JournalEntry
        fields = ['id', 'student', 'date', 'content', 'mentor_feedback', 'supervisor_feedback']

class StudentSerializer(serializers.ModelSerializer):
    journal_entries = JournalEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'username', 'internship_company', 'internship_start_date', 'internship_end_date', 'journal_entries']

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['id', 'name', 'email']

class AdviceSerializer(serializers.ModelSerializer):
    supervisor = serializers.StringRelatedField()
    student = serializers.StringRelatedField()

    class Meta:
        model = Advice
        fields = ['id', 'supervisor', 'student', 'advice', 'created_at']
