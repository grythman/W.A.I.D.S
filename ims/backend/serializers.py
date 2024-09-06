# ims/serializers.py
from rest_framework import serializers
from .models import FacultyProfile, StudentProfile, Internship, CustomUser

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyProfile
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'is_faculty', 'is_student']
