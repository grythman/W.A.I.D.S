from django.contrib import admin
from .models import Student, Mentor, JournalEntry

admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(JournalEntry)
