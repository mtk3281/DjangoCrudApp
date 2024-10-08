from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('laws/',include('laws.urls')),
    path('api/',include('apis.urls')),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")), 
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
]
