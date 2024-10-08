from django.urls import path
from .views import *
from django.urls import path, include
from .views import UserViewSet  # Assuming your UserViewSet is in the same views file
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from drf_spectacular.views import (
SpectacularAPIView,
SpectacularRedocView, # new
)
=======
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04

# Create the router
router = DefaultRouter()
router.register(r'records', RecordViewSet, basename='record')
router.register(r'users', UserViewSet, basename='user')  # Register UserViewSet if needed

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
<<<<<<< HEAD
    path("schema/", SpectacularAPIView.as_view(), name="schema"), # new
    path("schema/redoc/", SpectacularRedocView.as_view(
            url_name="schema"), name="redoc",),     
=======
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
]


# urlpatterns = [
#     path("", RecordListAPIView.as_view(), name="record-list"),
#     path("<int:pk>", RecordDetailAPIView.as_view(), name="record-detail"),
#     path('users/', UserViewSet, name='user-list'),
    
# ]