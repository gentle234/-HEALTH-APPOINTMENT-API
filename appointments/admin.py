from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'date', 'time', 'reason_for_visit', 'status']  # Keep 'status' in list_display
    list_filter = ['doctor', 'patient', 'date', 'status']  # Keep 'status' in list_filter

admin.site.register(Appointment, AppointmentAdmin)
