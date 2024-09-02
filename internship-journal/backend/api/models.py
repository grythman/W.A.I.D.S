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


class Student(AbstractUser):
    internship_company = models.CharField(max_length=255)
    internship_start_date = models.DateField()
    internship_end_date = models.DateField()

    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128, default='temporary_password')

    def register(self, username, password):
        self.username = username
        self.set_password(password)
        self.save()
    
    def login(self, username, password):
        if self.username == username and self.check_password(password):
            return True
        else:
            return False

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


class Supervisor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def give_advice(self, student, advice):
        Advice.objects.create(supervisor=self, student=student, advice=advice)

    def monitor_progress(self, student):
        journal_entries = JournalEntry.objects.filter(student=student)
        return journal_entries


class Advice(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    advice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)