from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PatientViewSet, DoctorViewSet, AppointmentViewSet, MedicalHistoryViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medicalhistories', MedicalHistoryViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
