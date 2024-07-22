from django.db import models
from django.contrib.auth.models import User

class InternshipEntry(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    work_done = models.TextField()
    supervisor_comment = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.username} - {self.date}"
