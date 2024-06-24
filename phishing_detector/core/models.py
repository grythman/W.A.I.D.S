
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone
import re
import validators


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='core_user_set',  # related_name-ийг өөрчлөх
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='core_user_set',  # related_name-ийг өөрчлөх
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_query_name='user',
    )

    def register(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email
        self.save()

    def login(self, username, password):
        user = User.objects.get(username=username)
        if user.check_password(password):
            return True
        return False

    def resetPassword(self, new_password):
        self.set_password(new_password)
        self.save()
        send_mail(
            'Password Reset',
            'Your password has been reset successfully.',
            'from@example.com',
            [self.email],
            fail_silently=False,
        )

class Email(models.Model):
    sender = models.EmailField()
    receiver = models.EmailField()
    subject = models.CharField(max_length=255)
    content = models.TextField()

    def checkPhishing(self):
        return self.analyzeContent()

    def analyzeContent(self):
        suspicious_words = ['urgent', 'lottery', 'click here', 'password']
        for word in suspicious_words:
            if re.search(r'\b' + word + r'\b', self.content, re.IGNORECASE):
                return True
        return False

class URL(models.Model):
    link = models.URLField()
    domain = models.CharField(max_length=255)

    def checkPhishing(self):
        return self.analyzeLink()

    def analyzeLink(self):
        return not validators.url(self.link)

class Report(models.Model):
    details = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    @staticmethod
    def generateReport(user, details):
        report = Report(user=user, details=details)
        report.save()
        return report

class Database:

    @staticmethod
    def saveData(instance):
        instance.save()

    @staticmethod
    def retrieveData(model_class, **filters):
        return model_class.objects.filter(**filters)

class PhishingDetector:

    @staticmethod
    def analyzeEmail(email):
        return email.checkPhishing()

    @staticmethod
    def analyzeURL(url):
        return url.checkPhishing()

class SpamAssassin:

    @staticmethod
    def checkSpam(content):
        spam_keywords = ['free', 'winner', 'credit', 'click']
        for keyword in spam_keywords:
            if keyword in content.lower():
                 return True
        return False
