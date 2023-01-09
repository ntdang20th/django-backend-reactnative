from .serializers import *
from rest_framework import viewsets

class WardModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class DistrictModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class ProvinceModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class ShareAddressModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShareAddress.objects.all()
    serializer_class = ShareAddressSerializer