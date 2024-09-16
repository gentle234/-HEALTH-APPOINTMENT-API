from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # Doctor assigned to the appointment
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # Patient assigned to the appointment
    date = models.DateField()  # Appointment date
    time = models.TimeField()  # Appointment time
    reason_for_visit = models.TextField(default="General Checkup")  # Reason for visit
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ('doctor', 'date', 'time')  # Ensure no double-booking for doctor at the same time

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.email} on {self.date} at {self.time}"
