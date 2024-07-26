from django.db import models
from django.contrib.auth.models import AbstractUser

class Mentor(models.Model):
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(unique=True, default="")

    def __str__(self):
        return self.name

    def give_feedback(self, journal_entry, feedback):
        if journal_entry.student.mentor == self:
            journal_entry.mentor_feedback = feedback
            journal_entry.save()
        else:
            raise ValueError("You are not authorized to give feedback for this student.")

    def evaluate_student(self, student, evaluation):
        if student.mentor == self:
            student.evaluation = evaluation
            student.save()
        else:
            raise ValueError("You are not authorized to evaluate this student.")

    def get_students(self):
        return self.students.all()

from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    internship_company = models.CharField(max_length=255)
    internship_start_date = models.DateField()
    internship_end_date = models.DateField()

    # related_name параметрийг нэмнэ
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    username = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=128, default='temporary_password')

    def log_activity(self, date, content):
        journal_entry = JournalEntry.objects.create(
            student=self,
            date=date,
            content=content,
        )
        return journal_entry

class JournalEntry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='journal_entries')
    date = models.DateField()
    content = models.TextField()
    mentor_feedback = models.TextField(blank=True, null=True)
    supervisor_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.username} - {self.date}"

    def add_feedback(self, feedback_type, feedback):
        if feedback_type == 'mentor':
            self.mentor_feedback = feedback
        elif feedback_type == 'supervisor':
            self.supervisor_feedback = feedback
        self.save()
