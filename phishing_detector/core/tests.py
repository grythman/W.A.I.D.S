from django.test import TestCase
from .models import User, Email, URL, Report

class ModelTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.assertEqual(user.email, 'test@example.com')

    def test_create_email(self):
        email = Email.objects.create(sender='test@example.com', receiver='receiver@example.com', subject='Test', content='This is a test email.')
        self.assertEqual(email.subject, 'Test')

    def test_create_url(self):
        url = URL.objects.create(link='http://example.com', domain='example.com')
        self.assertEqual(url.link, 'http://example.com')

    def test_create_report(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        report = Report.objects.create(user=user, details='This is a test report.')
        self.assertEqual(report.details, 'This is a test report.')
