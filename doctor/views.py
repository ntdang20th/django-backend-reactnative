from .serializers import *
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

import json
class DoctorModelViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

@csrf_exempt
def doctor_login(request):
    data = json.loads(request.body.decode('utf-8'))
    user = json.loads(json.dumps(data))
    print(user)
    if request.method == 'POST':
        username = user['username']
        password = user['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            doctor = Doctor.objects.get(user=user)
            doctor_serializer = DoctorSerializer(doctor)
            response = {'Success': 1, 
                        'Message': 'login success',
                        'data': doctor_serializer.data}
            return JsonResponse(response)
  
    response = {'Success': 0, 
                'Message': 'login fail'}
    return JsonResponse(response)
