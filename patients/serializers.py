from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['date_of_birth', 'address', 'emergency_contact_name', 'emergency_contact_phone', 'medical_history', 'allergies']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
