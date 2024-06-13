from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class HRManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class OnboardingTask(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='Pending')
    employee = models.ForeignKey(Employee, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Document(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')
    employee = models.ForeignKey(Employee, related_name='documents', on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class TrainingModule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    employee = models.ForeignKey(Employee, related_name='training_modules', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ITSupport(models.Model):
    resource_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')
    employee = models.ForeignKey(Employee, related_name='it_support', on_delete=models.CASCADE)

    def __str__(self):
        return self.resource_type

class Notification(models.Model):
    message = models.TextField()
    recipient = models.EmailField()

    def __str__(self):
        return self.message
