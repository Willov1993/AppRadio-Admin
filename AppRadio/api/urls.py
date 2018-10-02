# api/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('emisoras/', views.ListEmisora.as_view()),
    path('segmentos/', views.ListSegmento.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]