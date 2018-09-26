from django.urls import path
from . import views

app_name = 'webadminradio'

urlpatterns = [
    path('', views.home, name='home'), # Muestra la pantalla principal /webadmin/
    path('segmento/agregar', views.agregar_segmento, name="agregar_segmento"), # Muestra la pantalla para agregar segmento
    path('emisora/agregar', views.agregar_emisora, name="agregar_emisora") # Muestra la pantalla para agregar emisora
]
