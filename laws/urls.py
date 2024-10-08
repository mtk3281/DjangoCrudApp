# urls.py
from django.urls import path
from .views import law_retrieve, law_display

urlpatterns = [
    path('law_retrieve', law_retrieve, name='law_retrieve'),  # Renamed for clarity
    path('law-display/<int:year>/<int:number>/', law_display, name='law_display'),
]
