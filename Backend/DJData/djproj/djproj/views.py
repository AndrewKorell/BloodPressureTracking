from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny
from djapp.serializers import BpSerializer, PatientSerilizer
from djapp.models import BpMeasurement, Patient

import logging 

logger = logging.getLogger(__name__)

class BloodDataView(APIView):

    def get(self, request, pk, *args, **kwargs) :
        qs = BpMeasurement.objects.filter(patient_id=pk)
        serializer = BpSerializer(qs, many=True)

        return Response(serializer.data) 

    def post(self, request, pk, *args, **kwargs) :
        m1 = {
            
                'systolic': request.POST['systolic'],
                'diastolic':request.POST['diastolic'],
                'pulse': request.POST['pulse'],
                'note': request.POST['note'],
                'measDateTime':request.POST['measDateTime'],
                'patient': pk
        }
  
        serializer = BpSerializer(data=m1)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class PatientView(APIView):

    def get(self, request, pk, *args, **kwargs) :

        if pk == "all" :
            qs = Patient.objects.all()

            serializer = PatientSerilizer(qs, many=True)

            return Response(serializer.data)

        else :    
            qs = Patient.objects.filter(username=pk)
            
            serializer = PatientSerilizer(qs, many=True)
            
            return Response(serializer.data)


    # def get(self, request, pk, *args, **kwargs) :
    #     if request.name == 'patients' :

    #         qs = Patient.objects.all()
            
    #         serializer = PatientSerilizer(qs, many=True)
            
    #         return Response(serializer.data)
    #     elif request.name == 'patient' :

    #         qs = Patient.objects.filter(username=pk)

    #         serializer = PatientSerilizer(qs, many=False)

    #         return Response(serializer.data)
        

    def post(self, request, *args, **kwargs) :
        
        if Patient.objects.filter(username=request.POST['username']).exists() :
            return Response(data={ "Username %s already exists" %(request.POST['username']) })
        
        serializer = PatientSerilizer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)