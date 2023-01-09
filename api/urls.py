from django.urls import path, include
from .views import FollowUpView, ResponesData, LocationFollowUpView, ResponesLocation, showMap
urlpatterns = [
    path('status/', FollowUpView.as_view(), name='status'),
    path('map/', LocationFollowUpView.as_view(), name='location'),
    path('post/', ResponesData),
    path('location/', ResponesLocation),
    path('basemap', showMap.as_view(), name='map'),
]
