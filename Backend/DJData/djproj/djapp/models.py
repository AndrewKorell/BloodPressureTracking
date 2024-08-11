from django.db import models

class Patient(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField()


    def __str__(self):
        return f"{self.username}"
    

class BpMeasurement(models.Model):
    systolic = models.PositiveSmallIntegerField()
    diastolic = models.PositiveSmallIntegerField()
    pulse = models.PositiveSmallIntegerField()
    patient = models.ForeignKey(Patient, related_name="bp_measurements", on_delete=models.CASCADE)
    measDateTime = models.DateTimeField()
    logDateTime = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=500)

    def __str__(self):
        return 'BP: %d/%d Pulse:%d   %s' % (self.systolic, self.diastolic, self.pulse, self.measDateTime.strftime('%Y-%m-%d %H:%M'))

