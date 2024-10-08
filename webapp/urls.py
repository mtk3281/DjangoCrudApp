from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name=''),
    path('dashboard/', dashboard, name='dashboard'),
    path('create-record/', create_record, name='create-record'),
    path('update-record/<int:pk>/', update_record, name='update-record'),
    path('view-record/<int:pk>/', view_record, name='view-record'),
    path('delete-record/<int:pk>/', delete_record, name='delete-record'),
]
