from rest_framework import serializers
from .models import BpMeasurement, Patient

class BpSerializer(serializers.ModelSerializer):


    class Meta:
        model = BpMeasurement
        fields = [
            'systolic', 
            'diastolic', 
            'pulse',
            'patient', 
            'measDateTime', 
            'note'
        ]


class PatientSerilizer(serializers.ModelSerializer):
    bp_measurements = serializers.StringRelatedField(many=True)

    class Meta:
        model = Patient 
        fields = [
            'id',
            'username',
            'email',
            'bp_measurements', 
        ]