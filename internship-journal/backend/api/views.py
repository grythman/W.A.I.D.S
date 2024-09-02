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

class MentorCreate(generics.CreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorUpdate(generics.UpdateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorDelete(generics.DestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDelete(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class JournalEntryList(generics.ListCreateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalEntryCreate(generics.CreateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalEntryUpdate(generics.UpdateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalEntryDelete(generics.DestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class SupervisorList(generics.ListCreateAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class SupervisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class SupervisorCreate(generics.CreateAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class SupervisorUpdate(generics.UpdateAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class SupervisorDelete(generics.DestroyAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class AdviceList(generics.ListCreateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class AdviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class AdviceCreate(generics.CreateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class AdviceUpdate(generics.UpdateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class AdviceDelete(generics.DestroyAPIView):
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