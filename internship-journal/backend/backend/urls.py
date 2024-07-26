from django.contrib import admin
from django.urls import path
from journal.views import login_view, register_view, journal_entries, evaluate_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login_view),
    path('api/register', register_view),
    path('api/journal', journal_entries),
    path('api/evaluate/<int:student_id>', evaluate_student),
]
