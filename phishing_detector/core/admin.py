from django.contrib import admin
from .models import User, Email, URL, Report

admin.site.register(User)
admin.site.register(Email)
admin.site.register(URL)
admin.site.register(Report)
