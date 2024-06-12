from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HRManager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class OnboardingTask(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Document(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class TrainingModule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class ITSupport(models.Model):
    resource_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.resource_type

class Notification(models.Model):
    message = models.TextField()
    recipient = models.EmailField()

    def __str__(self):
        return self.recipient
