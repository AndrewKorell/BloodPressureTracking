from django.db import models

class BpMeasurement(models.Model):
    systolic = models.PositiveSmallIntegerField()
    diastolic = models.PositiveSmallIntegerField()
    pulse = models.PositiveSmallIntegerField()
    patientId = models.PositiveIntegerField()
    measDateTime = models.DateTimeField()
    logDateTime = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=500)

class Patient(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()

