from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from djapp.serializers import BpSerializer
from djapp.models import BpMeasurement

class BloodDataView(APIView):

    def get(self, request, *args, **kwargs) :
        qs = BpMeasurement.objects.all()
        bp1 = qs.first()
        serializer = BpSerializer(bp1)

        return Response(serializer.data) 

    def post(self, request, *args, **kwargs) :
        serializer = BpSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
