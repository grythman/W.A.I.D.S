from django.contrib import admin
from .models import Employee, HRManager, OnboardingTask, Document, TrainingModule, ITSupport, Notification

admin.site.register(Employee)
admin.site.register(HRManager)
admin.site.register(OnboardingTask)
admin.site.register(Document)
admin.site.register(TrainingModule)
admin.site.register(ITSupport)
admin.site.register(Notification)
