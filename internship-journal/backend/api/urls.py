from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, MentorViewSet, JournalEntryViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'mentors', MentorViewSet)
router.register(r'journal-entries', JournalEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
