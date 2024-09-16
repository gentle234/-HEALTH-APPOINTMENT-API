from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import AppointmentSerializer
from .models import Appointment

class AppointmentListCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            # Save the appointment with the correct doctor/patient relationships
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Patients should see only their appointments; doctors see theirs
        if request.user.is_doctor:
            appointments = Appointment.objects.filter(doctor__user=request.user)
        else:
            appointments = Appointment.objects.filter(patient__user=request.user)

        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AppointmentDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request, pk):
        """
        Retrieve a specific appointment by its primary key (ID).
        """
        try:
            appointment = Appointment.objects.get(pk=pk)

            # Ensure the user is the doctor or patient tied to the appointment
            if appointment.doctor.user != request.user and appointment.patient.user != request.user:
                return Response({"detail": "You do not have permission to view this appointment."}, status=status.HTTP_403_FORBIDDEN)

            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response({"detail": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """
        Delete a specific appointment by its primary key (ID).
        """
        try:
            appointment = Appointment.objects.get(pk=pk)

            # Ensure the user is the doctor or patient tied to the appointment
            if appointment.doctor.user != request.user and appointment.patient.user != request.user:
                return Response({"detail": "You do not have permission to delete this appointment."}, status=status.HTTP_403_FORBIDDEN)

            appointment.delete()
            return Response({"detail": "Appointment deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response({"detail": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
# Create your views here.
