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
    print(request.method)
    # username = request.POST['username']
    # password = request.POST['password']
    username = "doctor1"
    password = '@D12346'
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        response = {'Success': 1, 
                    'Message': 'login success'}
        return JsonResponse(response)
    else:
        response = {'Success': 0, 
                    'Message': 'login fail'}
        return JsonResponse(response)
