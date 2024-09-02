# admin.py
from django.contrib import admin
from .models import Mentor, Student, JournalEntry, Supervisor, Advice

class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'internship_company', 'internship_start_date', 'internship_end_date')
    search_fields = ('username', 'internship_company')
    list_filter = ('internship_start_date', 'internship_end_date')

class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'content', 'mentor_feedback', 'supervisor_feedback')
    search_fields = ('student__username', 'content')
    list_filter = ('date',)

class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class AdviceAdmin(admin.ModelAdmin):
    list_display = ('supervisor', 'student', 'advice', 'created_at')
    search_fields = ('supervisor__name', 'student__username', 'advice')
    list_filter = ('created_at',)

admin.site.register(Mentor, MentorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(JournalEntry, JournalEntryAdmin)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Advice, AdviceAdmin)