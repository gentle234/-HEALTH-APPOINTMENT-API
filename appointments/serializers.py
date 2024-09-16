from rest_framework import serializers
from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), required=False)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), required=False)


    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'time', 'reason_for_visit', 'status']
        extra_kwargs = {
            'doctor': {'read_only': True},  # Ensuring it's set based on the request
            'patient': {'read_only': True}  # Ensuring it's set based on the user
        }

    def validate(self, data):
        # Ensure no overlapping appointments for the doctor
        if Appointment.objects.filter(doctor=data['doctor'], date=data['date'], time=data['time']).exists():
            raise serializers.ValidationError("Doctor already has an appointment at this time.")
        return data

    def create(self, validated_data):
        user = self.context['request'].user

        # Handle patient booking
        if user.is_patient:
            if not hasattr(user, 'patient'):
                raise serializers.ValidationError("User does not have a patient profile.")
            validated_data['patient'] = user.patient

        # Handle doctor scheduling
        elif user.is_doctor:
            if not hasattr(user, 'doctor'):
                raise serializers.ValidationError("User does not have a doctor profile.")
            validated_data['doctor'] = user.doctor

        else:
            raise serializers.ValidationError("Only patients or doctors can book or schedule appointments.")

        return super().create(validated_data)