# ims/views.py
from rest_framework import viewsets
from .models import FacultyProfile, StudentProfile, Internship, CustomUser
from .serializers import FacultySerializer, StudentSerializer, InternshipSerializer, UserSerializer

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = FacultyProfile.objects.all()
    serializer_class = FacultySerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer

class InternshipViewSet(viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
