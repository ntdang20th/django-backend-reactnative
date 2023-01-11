from .serializers import *
from rest_framework import viewsets

from django.views.decorators.csrf import csrf_exempt

import json
class DoctorModelViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
