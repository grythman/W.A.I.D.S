# admin.py
from django.contrib import admin
from .models import Mentor, Student, JournalEntry, Supervisor, Advice

class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'content')

admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(JournalEntry, JournalEntryAdmin)
admin.site.register(Supervisor)
admin.site.register(Advice)