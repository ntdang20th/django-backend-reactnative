from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()

#register views with router
router.register(r'doctor', DoctorModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]