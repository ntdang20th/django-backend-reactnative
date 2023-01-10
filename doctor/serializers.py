from rest_framework import  serializers
from django.contrib.auth import get_user_model

from backend import settings
from .models import Doctor


class userSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'email',
            'first_name',
            'last_name')
        model=get_user_model()

        
class DoctorSerializer(serializers.ModelSerializer):
    user = userSerializer(read_only=True)
    class Meta:
        model = Doctor
        fields = ['user', 'phone_number', 'share_address', 'hospital_name']
        
