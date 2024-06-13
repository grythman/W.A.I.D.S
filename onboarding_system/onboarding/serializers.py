from rest_framework import serializers
from .models import Employee, HRManager, OnboardingTask, Document, TrainingModule, ITSupport, Notification
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'user', 'position']

class HRManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = HRManager
        fields = ['id', 'user']

class OnboardingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnboardingTask
        fields = ['id', 'description', 'status', 'employee']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'type', 'status', 'employee']

class TrainingModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingModule
        fields = ['id', 'title', 'description', 'status', 'employee']

class ITSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITSupport
        fields = ['id', 'resource_type', 'status', 'employee']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'recipient']
