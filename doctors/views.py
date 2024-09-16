from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import DoctorSerializer

class DoctorProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not request.user.is_doctor:
            return Response({"detail": "Only doctors can create this profile."}, status=status.HTTP_403_FORBIDDEN)

        serializer = DoctorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Doctor profile created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

