from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()

#register views with router
router.register(r'unit', UnitModelViewSet)
router.register(r'acceleration', AccelerationModelViewSet)
router.register(r'gyroscope', GyroscopeModelViewSet)
router.register(r'rotation', RotationModelViewSet)
router.register(r'touch-status', TouchStatusModelViewSet)
router.register(r'location', LocationModelViewSet)
router.register(r'rawdata', RawdataModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]