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

from django.contrib.auth import logout

class StudentLogout(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

class StudentProfile(generics.RetrieveAPIView):
    serializer_class = StudentSerializer

    def get_object(self):
        return self.request.user

class StudentProfileUpdate(generics.UpdateAPIView):
    serializer_class = StudentSerializer

    def get_object(self):
        return self.request.user

class StudentProfileDelete(generics.DestroyAPIView):
    serializer_class = StudentSerializer

    def get_object(self):
        return self.request.user

# views.py
class StudentMentorList(generics.ListCreateAPIView):
    serializer_class = MentorSerializer

    def get_queryset(self):
        return Mentor.objects.filter(student=self.request.user)

class StudentMentorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class StudentMentorCreate(generics.CreateAPIView):
    serializer_class = MentorSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class StudentMentorUpdate(generics.UpdateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class StudentMentorDelete(generics.DestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class StudentJournalEntryList(generics.ListCreateAPIView):
    serializer_class = JournalEntrySerializer

    def get_queryset(self):
        return JournalEntry.objects.filter(student=self.request.user)

class StudentJournalEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class StudentJournalEntryCreate(generics.CreateAPIView):
    serializer_class = JournalEntrySerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class StudentJournalEntryUpdate(generics.UpdateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class StudentJournalEntryDelete(generics.DestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class StudentAdviceList(generics.ListCreateAPIView):
    serializer_class = AdviceSerializer

    def get_queryset(self):
        return Advice.objects.filter(student=self.request.user)

class StudentAdviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class StudentAdviceCreate(generics.CreateAPIView):
    serializer_class = AdviceSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class StudentAdviceUpdate(generics.UpdateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class StudentAdviceDelete(generics.DestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class StudentSupervisorList(generics.ListCreateAPIView):
    serializer_class = SupervisorSerializer

    def get_queryset(self):
        return Supervisor.objects.filter(student=self.request.user)

class StudentSupervisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class StudentSupervisorCreate(generics.CreateAPIView):
    serializer_class = SupervisorSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class StudentSupervisorUpdate(generics.UpdateAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class StudentSupervisorDelete(generics.DestroyAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

# views.py
class StudentMentorAssign(APIView):
    def post(self, request):
        mentor_id = request.data.get('mentor_id')
        mentor = Mentor.objects.get(id=mentor_id)
        mentor.student = request.user
        mentor.save()
        return Response({'message': 'Mentor assigned successfully'}, status=status.HTTP_200_OK)

class StudentMentorUnassign(APIView):
    def post(self, request):
        mentor_id = request.data.get('mentor_id')
        mentor = Mentor.objects.get(id=mentor_id)
        mentor.student = None
        mentor.save()
        return Response({'message': 'Mentor unassigned successfully'}, status=status.HTTP_200_OK)

class StudentJournalEntryAssign(APIView):
    def post(self, request):
        journal_entry_id = request.data.get('journal_entry_id')
        journal_entry = JournalEntry.objects.get(id=journal_entry_id)
        journal_entry.student = request.user
        journal_entry.save()
        return Response({'message': 'Journal entry assigned successfully'}, status=status.HTTP_200_OK)

class StudentJournalEntryUnassign(APIView):
    def post(self, request):
        journal_entry_id = request.data.get('journal_entry_id')
        journal_entry = JournalEntry.objects.get(id=journal_entry_id)
        journal_entry.student = None
        journal_entry.save()
        return Response({'message': 'Journal entry unassigned successfully'}, status=status.HTTP_200_OK)

class StudentAdviceAssign(APIView):
    def post(self, request):
        advice_id = request.data.get('advice_id')
        advice = Advice.objects.get(id=advice_id)
        advice.student = request.user
        advice.save()
        return Response({'message': 'Advice assigned successfully'}, status=status.HTTP_200_OK)

class StudentAdviceUnassign(APIView):
    def post(self, request):
        advice_id = request.data.get('advice_id')
        advice = Advice.objects.get(id=advice_id)
        advice.student = None
        advice.save()
        return Response({'message': 'Advice unassigned successfully'}, status=status.HTTP_200_OK)

class StudentSupervisorAssign(APIView):
    def post(self, request):
        supervisor_id = request.data.get('supervisor_id')
        supervisor = Supervisor.objects.get(id=supervisor_id)
        supervisor.student = request.user
        supervisor.save()
        return Response({'message': 'Supervisor assigned successfully'}, status=status.HTTP_200_OK)

class StudentSupervisorUnassign(APIView):
    def post(self, request):
        supervisor_id = request.data.get('supervisor_id')
        supervisor = Supervisor.objects.get(id=supervisor_id)
        supervisor.student = None
        supervisor.save()
        return Response({'message': 'Supervisor unassigned successfully'}, status=status.HTTP_200_OK)