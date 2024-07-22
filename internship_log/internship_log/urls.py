from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import InternshipEntryViewSet

router = DefaultRouter()
router.register(r'internship-entries', InternshipEntryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
