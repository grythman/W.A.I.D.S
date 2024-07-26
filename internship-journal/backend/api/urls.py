from django.urls import path
from . import views

urlpatterns = [
    path('mentors/', views.MentorList.as_view(), name='mentor_list'),
    path('mentors/<int:pk>/', views.MentorDetail.as_view(), name='mentor_detail'),
    path('students/', views.StudentList.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
    path('journal-entries/', views.JournalEntryList.as_view(), name='journal_entry_list'),
    path('journal-entries/<int:pk>/', views.JournalEntryDetail.as_view(), name='journal_entry_detail'),
    path('supervisors/', views.SupervisorList.as_view(), name='supervisor_list'),
    path('supervisors/<int:pk>/', views.SupervisorDetail.as_view(), name='supervisor_detail'),
    path('advice/', views.AdviceList.as_view(), name='advice_list'),
    path('advice/<int:pk>/', views.AdviceDetail.as_view(), name='advice_detail'),
    path('register/', views.StudentRegister.as_view(), name='student_register'),
    path('login/', views.StudentLogin.as_view(), name='student_login'),
]