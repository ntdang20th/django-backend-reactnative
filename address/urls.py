from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()

#register views with router
router.register(r'ward', WardModelViewSet)
router.register(r'district', DistrictModelViewSet)
router.register(r'province', ProvinceModelViewSet)
router.register(r'share-address', ShareAddressModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]