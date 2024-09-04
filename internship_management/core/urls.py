from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AdminViewSet, StudentViewSet, MentorViewSet, SessionViewSet, ContentViewSet, JournalViewSet, MonitoringViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'students', StudentViewSet)
router.register(r'mentors', MentorViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'journals', JournalViewSet)
router.register(r'monitorings', MonitoringViewSet)

urlpatterns = [
    path('', include(router.urls)),
]