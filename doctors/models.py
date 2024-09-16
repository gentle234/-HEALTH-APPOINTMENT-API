from django.db import models
from custom_user.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    qualifications = models.TextField()
    hospital_affiliation = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Dr. {self.user.first_name} - {self.specialty}"
