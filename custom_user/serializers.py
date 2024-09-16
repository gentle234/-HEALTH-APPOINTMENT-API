from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'is_doctor', 'is_patient']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_doctor=validated_data.get('is_doctor', False),
            is_patient=validated_data.get('is_patient', False)
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
