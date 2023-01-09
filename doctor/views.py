from .serializers import *
from rest_framework import viewsets

class DoctorModelViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

