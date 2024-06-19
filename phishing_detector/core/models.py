from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',  # related_name нэмэх
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_permission_set',  # related_name өөрчлөх
        related_query_name='custom_user_permission',
    )

class Email(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    is_phishing = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

class URL(models.Model):
    link = models.URLField()
    domain = models.CharField(max_length=255)
    is_phishing = models.BooleanField(default=False)

    def __str__(self):
        return self.link

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.user.username} on {self.timestamp}"
