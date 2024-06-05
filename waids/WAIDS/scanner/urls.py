# scanner/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scan_report/', views.scan_report, name='scan_report'),
    path('attack_list/', views.attack_list, name='attack_list'),
]
