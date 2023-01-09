

from .serializers import *
from .models import *
from rest_framework import viewsets

class UnitModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class AccelerationModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Acceleration.objects.all()
    serializer_class = AccelerationSerializer

class GyroscopeModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gyroscope.objects.all()
    serializer_class = GyroscopeSerializer

class RotationModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rotation.objects.all()
    serializer_class = RotationSerializer

class TouchStatusModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TouchStatus.objects.all()
    serializer_class = TouchStatusSerializer
    
class LocationModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class RawdataModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rawdata.objects.all()
    serializer_class = RawdataSerializer