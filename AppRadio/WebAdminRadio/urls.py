from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('segmento/agregar', views.agregar_segmento, name="ag_segmento")
]