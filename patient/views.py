import json
from django.shortcuts import render

from address.models import *
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
    # filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    # filterset_fields = ['device']
    # ordering_fields = ['device', 'doctor']
    
    def get_queryset(self):
        qs = super(PatientModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
            return qs
        user = self.request.user
        doctor = Doctor.objects.get(user=user)
        return qs.filter(doctor=doctor)

class HasPatientFamiliarModelViewSet(viewsets.ModelViewSet):
    queryset = HasPatientFamiliar.objects.all()
    serializer_class = HasPatientFamiliarSerializer
    
    def get_queryset(self):
        qs = super(HasPatientFamiliarModelViewSet, self).get_queryset()
        if self.request.user.is_superuser:
            return qs
        user = self.request.user
        doctor = Doctor.objects.get(user=user)
        patients = Patient.objects.filter(doctor=doctor)
        return qs.filter(patient__in=patients)

@csrf_exempt
def add_patient(request):
    data = json.loads(request.body.decode('utf-8'))
    req = json.loads(json.dumps(data))
    if request.method == 'POST' and not request.user.is_superuser and request.user:
        uuid = req['uuid']
        last_name = req['last_name']
        first_name = req['first_name']
        gender = req['gender']
        birth = req['birth']
        phone_number = req['phone_number']
        address = req['address']
        picture = req['picture']

        try:
            #add address
            address = ShareAddress.objects.create(
                address = address,
                ward = Ward.objects.get(pk=1),
                district = District.objects.get(pk=1),
                province = Province.objects.get(pk=1),
            )
            #add patient info
            patient_info = PatientInfo.objects.create(
                last_name = last_name,
                first_name = first_name,
                gender =gender,
                birth = birth,
                phone_number = phone_number,
                share_address = address,
                profile_picture = picture
            )
            
            #add patient
            patient = Patient.objects.create(
                doctor = Doctor.objects.get(pk=1),
                patient_info = patient_info 
            )
            
            #add device
            device = Device.objects.create(
                patient = patient,
                uuid = uuid,
                description = 'no',
            )
            
            response = {'Success': 1, 
                        'Message': 'create success'}
            return JsonResponse(response)
        
        except Exception as e:
            response = {'Success': 0, 
                        'Message': str(e)}
            return JsonResponse(response)
        
@csrf_exempt
def delete_patient(request):
    data = json.loads(request.body.decode('utf-8'))
    req = json.loads(json.dumps(data))
    if request.method == 'POST' and not request.user.is_superuser and request.user:
        uuid = req['uuid']
        last_name = req['last_name']
        first_name = req['first_name']
        gender = req['gender']
        birth = req['birth']
        phone_number = req['phone_number']
        address = req['address']
        picture = req['picture']

        try:
            device = Device.objects.get(uuid)
            address = ShareAddress.objects.get(address=address)

            
            response = {'Success': 1, 
                        'Message': 'create success'}
            return JsonResponse(response)
        
        except Exception as e:
            response = {'Success': 0, 
                        'Message': str(e)}
            return JsonResponse(response)