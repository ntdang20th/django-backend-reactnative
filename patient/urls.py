from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()

#register views with router
router.register(r'device', DeviceModelViewSet)
router.register(r'familiar', FamiliarModelViewSet)
router.register(r'patient-info', PatientInfoModelViewSet)
router.register(r'patient', PatientModelViewSet)
router.register(r'has-patient-familiar', HasPatientFamiliarModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
