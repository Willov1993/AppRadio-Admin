from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('segmento/agregar', views.agregar_segmento, name="ag_segmento"),
    path('emisora/agregar', views.agregar_emisora, name="agregar_emisora")
]
