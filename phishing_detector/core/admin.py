from django.contrib import admin
from .models import User, Email, URL, Report, Database, SpamAssassin, PhishingDetector

admin.site.register(User)
admin.site.register(Email)
admin.site.register(URL)
admin.site.register(Report)
