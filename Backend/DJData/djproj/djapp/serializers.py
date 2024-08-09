from rest_framework import serializers
from .models import BpMeasurement

class BpSerializer(serializers.ModelSerializer):
    class Meta:
        model = BpMeasurement
        fields = [
            'systolic', 
            'diastolic', 
            'pulse', 
            'patientId', 
            'measDateTime', 
            'note'
        ]
        


    # systolic = models.PositiveSmallIntegerField()
    # diatolic = models.PositiveSmallIntegerField()
    # pulse = models.PositiveSmallIntegerField()
    # patientId = models.PositiveIntegerField()
    # testDateTime = models.DateTimeField()
    # note = models.CharField(max_length=500)