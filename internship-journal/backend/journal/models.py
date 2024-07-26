from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    internship_company = models.CharField(max_length=100)
    internship_start_date = models.DateField()
    internship_end_date = models.DateField()

class JournalEntry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    mentor_feedback = models.TextField(null=True, blank=True)
    supervisor_feedback = models.TextField(null=True, blank=True)

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def evaluate_student(self, student, evaluation):
        student.journalentry_set.update(mentor_feedback=evaluation)
        
    def get_students(self):
        return Student.objects.filter(journalentry__mentor_feedback__isnull=False).distinct()

class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def give_advice(self, student, advice):
        student.journalentry_set.update(supervisor_feedback=advice)
        
    def get_students(self):
        return Student.objects.filter(journalentry__supervisor_feedback__isnull=False).distinct()
