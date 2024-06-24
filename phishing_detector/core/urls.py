from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check-email/', views.check_email, name='check_email'),
    path('check-url/', views.check_url, name='check_url'),
    path('report/<int:report_id>/', views.report, name='report'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]