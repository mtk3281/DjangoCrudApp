from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('my-login/', mylogin, name='my-login'),
    path('logout/', user_logout, name='user-logout'),
]
