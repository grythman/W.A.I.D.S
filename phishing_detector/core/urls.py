from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('', views.home, name='home'),
    path('check-email/', views.check_email, name='check_email'),
    path('check-url/', views.check_url, name='check_url'),
    path('report/<int:report_id>/', views.report, name='report'),
    path('register/', views.register, name='register'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
