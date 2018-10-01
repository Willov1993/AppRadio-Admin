from django.urls import path
from . import views

app_name = 'webadminradio'

urlpatterns = [
    path('', views.home, name='home'), # Muestra la pantalla principal /webadmin/
    path('segmentos', views.segmentos, name='segmentos'), # Página principal donde se muestran los segmentos
    path('emisoras', views.emisoras, name='emisoras'), #Pagina donde se muestran las emisoras
    path('segmentos/agregar', views.agregar_segmento, name="agregar_segmento"), # Muestra la pantalla para agregar segmento
    path('emisoras/agregar', views.agregar_emisora, name="agregar_emisora") # Muestra la pantalla para agregar emisora
]
