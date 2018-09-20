from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('WebAdmin/', include('WebAdminRadio.urls')), # WebAdmin es un placeholder para no confundirlo con el default
]
