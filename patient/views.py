from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from doctor.models import Doctor


class DeviceModelViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'view-device'

class FamiliarModelViewSet(viewsets.ModelViewSet):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer

class PatientInfoModelViewSet(viewsets.ModelViewSet):
    queryset = PatientInfo.objects.all()
    serializer_class = PatientInfoSerializer

class PatientModelViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['device']
    ordering_fields = ['device', 'doctor']


class HasPatientFamiliarModelViewSet(viewsets.ModelViewSet):
    queryset = HasPatientFamiliar.objects.all()
    serializer_class = HasPatientFamiliarSerializer