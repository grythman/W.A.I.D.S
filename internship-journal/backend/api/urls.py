from django.urls import path
from . import views

urlpatterns = [
    path('mentors/', views.MentorList.as_view(), name='mentor_list'),
    path('mentors/<int:pk>/', views.MentorDetail.as_view(), name='mentor_detail'),
    path('mentors/create/', views.MentorCreate.as_view(), name='mentor_create'),
    path('mentors/<int:pk>/update/', views.MentorUpdate.as_view(), name='mentor_update'),
    path('mentors/<int:pk>/delete/', views.MentorDelete.as_view(), name='mentor_delete'),

    path('students/', views.StudentList.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
    path('students/create/', views.StudentCreate.as_view(), name='student_create'),
    path('students/<int:pk>/update/', views.StudentUpdate.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDelete.as_view(), name='student_delete'),

    path('journal-entries/', views.JournalEntryList.as_view(), name='journal_entry_list'),
    path('journal-entries/<int:pk>/', views.JournalEntryDetail.as_view(), name='journal_entry_detail'),
    path('journal-entries/create/', views.JournalEntryCreate.as_view(), name='journal_entry_create'),
    path('journal-entries/<int:pk>/update/', views.JournalEntryUpdate.as_view(), name='journal_entry_update'),
    path('journal-entries/<int:pk>/delete/', views.JournalEntryDelete.as_view(), name='journal_entry_delete'),

    path('supervisors/', views.SupervisorList.as_view(), name='supervisor_list'),
    path('supervisors/<int:pk>/', views.SupervisorDetail.as_view(), name='supervisor_detail'),
    path('supervisors/create/', views.SupervisorCreate.as_view(), name='supervisor_create'),
    path('supervisors/<int:pk>/update/', views.SupervisorUpdate.as_view(), name='supervisor_update'),
    path('supervisors/<int:pk>/delete/', views.SupervisorDelete.as_view(), name='supervisor_delete'),

    path('advice/', views.AdviceList.as_view(), name='advice_list'),
    path('advice/<int:pk>/', views.AdviceDetail.as_view(), name='advice_detail'),
    path('advice/create/', views.AdviceCreate.as_view(), name='advice_create'),
    path('advice/<int:pk>/update/', views.AdviceUpdate.as_view(), name='advice_update'),
    path('advice/<int:pk>/delete/', views.AdviceDelete.as_view(), name='advice_delete'),

    path('register/', views.StudentRegister.as_view(), name='student_register'),
    path('login/', views.StudentLogin.as_view(), name='student_login'),
]