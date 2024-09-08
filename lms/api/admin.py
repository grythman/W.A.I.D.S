from django.contrib import admin
from .models import Profile, Role, Course, Lesson, Lecture, Enroll

admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Lecture)
admin.site.register(Enroll)
