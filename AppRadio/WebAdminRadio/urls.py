from django.urls import path
from . import views

app_name = 'webadminradio'

urlpatterns = [
    path('', views.home, name='home'), # Muestra la pantalla principal /webadmin/
    path('segmentos', views.segmentos, name='segmentos'), # Página principal donde se muestran los segmentos
    path('emisoras', views.emisoras, name='emisoras'), #Pagina donde se muestran las emisoras
    path('publicidad', views.publicidad, name='publicidad'), #Pagina principal donde se muestra la publicidad.
    path('segmentos/agregar', views.agregar_segmento, name="agregar_segmento"), # Muestra la pantalla para agregar segmento
    path('emisoras/agregar', views.agregar_emisora, name="agregar_emisora"), # Muestra la pantalla para agregar emisora
    path('publicidad/agregar', views.agregar_publicidad, name = 'agregar_publicidad'), #Muestra la pantalla para agregar publicidad.
    path('emisoras/<int:id_emisora>/modificar', views.modificar_emisora, name='modificar_emisora'), # Muestra la pantalla para modificar emisora
    path('segmentos/<int:id_segmento>', views.ver_segmento, name="ver_segmento"), # Muestra la información un segmento
    path('segmentos/<int:id_segmento>/editar', views.modificar_segmento, name="editar_segmento"), # Muestra la pantalla para modificar un segmento
    path('locutores', views.locutores, name='locutores'), # Página principal donde se muestran los locutores.
    path('locutores/agregar', views.agregar_locutor, name="agregar_locutor"), # Página para agregar locutores.
    path('locutores/<int:id_locutor>', views.ver_locutor, name="ver_locutor")
]
