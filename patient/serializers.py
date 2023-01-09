from rest_framework import  serializers
from .models import *
from doctor.serializers import DoctorSerializer

from address.serializers import ShareAddressSerializer


class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'

class PatientInfoSerializer(serializers.ModelSerializer):
    share_address = ShareAddressSerializer(read_only=True)
    class Meta:
        model = PatientInfo
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient_info = PatientInfoSerializer(read_only=True)
    class Meta:
        model = Patient
        fields = ['doctor', 'patient_info']

class HasPatientFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HasPatientFamiliar
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = Device
        fields = ['uuid', 'patient', 'crutch']