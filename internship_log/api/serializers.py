from rest_framework import serializers
from .models import InternshipEntry

class InternshipEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipEntry
        fields = '__all__'