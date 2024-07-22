from rest_framework import viewsets
from .models import InternshipEntry
from .serializers import InternshipEntrySerializer

class InternshipEntryViewSet(viewsets.ModelViewSet):
    queryset = InternshipEntry.objects.all()
    serializer_class = InternshipEntrySerializer
