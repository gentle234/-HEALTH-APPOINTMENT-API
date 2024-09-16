from django.db import models
from custom_user.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    medical_history = models.TextField()
    allergies = models.TextField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - Patient'
