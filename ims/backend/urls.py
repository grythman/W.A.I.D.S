# ims_backend/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ims import views

router = DefaultRouter()
router.register(r'faculty', views.FacultyViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'internships', views.InternshipViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
