from django.urls import path
from . import views

urlpatterns = [
    path('request_onboarding/', views.request_onboarding, name='request_onboarding'),
    path('assign_task/', views.assign_task, name='assign_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('submit_document/<int:document_id>/', views.submit_document, name='submit_document'),
    path('complete_module/<int:module_id>/', views.complete_module, name='complete_module'),
    path('setup_it_resources/', views.setup_it_resources, name='setup_it_resources'),
    path('send_notification/', views.send_notification, name='send_notification'),
    path('employees/', views.employee_list, name='employee_list'),
]
