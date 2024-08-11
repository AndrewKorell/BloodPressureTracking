from django.contrib import admin
from .models import BpMeasurement, Patient

# Register your models here.
admin.site.register(BpMeasurement)
admin.site.register(Patient)