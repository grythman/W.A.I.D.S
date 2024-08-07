# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mentor, Student, JournalEntry, Supervisor, Advice
from .serializers import (
    MentorSerializer, StudentSerializer, JournalEntrySerializer,
    SupervisorSerializer, AdviceSerializer
)

class MentorList(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class JournalEntryList(generics.ListCreateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class SupervisorList(generics.ListCreateAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class SupervisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class AdviceList(generics.ListCreateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class AdviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class StudentRegister(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentLogin(APIView):
    def post(self, request):
        # Add your login logic here
        # For example:
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            student = Student.objects.get(username=username)
            if student.check_password(password):
                return Response({'message': 'Login successful'})
            else:
                return Response({'message': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        except Student.DoesNotExist:
            return Response({'message': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)