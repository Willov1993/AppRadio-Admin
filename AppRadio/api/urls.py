# api/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('segmentos/', views.ListSegmento.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]