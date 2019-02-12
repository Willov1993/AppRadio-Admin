from django.urls import path
from . import views

app_name = 'webadminradio'


urlpatterns = [
    path('', views.home, name='home'), # Muestra la pantalla principal /webadmin/
    path('segmentos', views.segmentos, name='segmentos'), # Página principal donde se muestran los segmentos
    path('segmentos/agregar', views.agregar_segmento, name="agregar_segmento"), # Muestra la pantalla para agregar segmento
    path('segmentos/<int:id_segmento>', views.ver_segmento, name="ver_segmento"), # Muestra la información un segmento
    path('segmentos/<int:id_segmento>/editar', views.modificar_segmento, name="editar_segmento"), # Muestra la pantalla para modificar un segmento
    path('segmentos/<int:id_segmento>/eliminar', views.borrar_segmento, name="borrar_segmento"), # URL para borrar un segmento
    path('emisoras', views.emisoras, name='emisoras'), #Pagina donde se muestran las emisoras
    path('emisoras/agregar', views.agregar_emisora, name="agregar_emisora"), # Muestra la pantalla para agregar emisora
    path('emisoras/<int:id_emisora>/editar', views.modificar_emisora, name='editar_emisora'), # Muestra la pantalla para modificar emisora
    path('emisoras/<int:id_emisora>/eliminar', views.borrar_emisora, name="borrar_emisora"), # URL para borrar un segmento
    path('publicidad/agregar', views.agregar_publicidad, name = 'agregar_publicidad'), #Muestra la pantalla para agregar publicidad.
    path('publicidad', views.publicidad, name='publicidad'), #Pagina principal donde se muestra la publicidad.
    path('publicidad/<int:id_publicidad>', views.ver_publicidad, name = 'ver_publicidad'),
    path('publicidad/<int:id_publicidad>/editar', views.modificar_publicidad, name = 'editar_publicidad'),
    path('publicidad/<int:id_publicidad>/eliminar', views.borrar_publicidad, name="borrar_publicidad"), # URL para borrar un segmento
    path('locutores', views.locutores, name='locutores'), # Página principal donde se muestran los locutores.
    path('locutores/asignar', views.asignar_locutor, name='asignar_locutor'), # Página para asignar un usuario como locutor de una radio.
    path('locutores/<int:id_locutor>', views.ver_locutor, name="ver_locutor"), # Página para mostrar la información de un locutor
    path('locutores/<int:id_locutor>/editar', views.modificar_locutor, name='editar_locutor'), # Página para modificar los locutores
    path('locutores/<int:id_locutor>/eliminar', views.borrar_locutor, name='borrar_locutor'), # URL para borrar un locutor
    path('locutores/asignar/<int:id_locutor>/segmento/<int:id_segmento>', views.asignar_locutor_segmento, name="asignar_locutor_segmento"), # Este URL permite asignar un usuario como locuor a un segmento
    path('usuarios', views.usuarios, name='usuarios'), # URL para ver los usuarios del sistema,
    path('usuarios/agregar', views.agregar_usuario, name='agregar_usuario'), # Form para agregar un usuario nuevo
    path('usuarios/<int:id_usuario>', views.ver_usuario, name='ver_usuario'), # URL para ver la informacion del usuario
    path('usuarios/<int:id_usuario>/editar', views.modificar_usuario, name='editar_usuario'), # URL para editar usuarios
    path('usuarios/<int:id_usuario>/eliminar', views.borrar_usuario, name='borrar_usuario'), # URL para eliminar un usuario
    path('sugerencias', views.sugerencias, name="sugerencias"), # URL para ver las sugerencias
    path('concursos/', views.concursos, name="concursos"), # URL para agregar concursos
    path('concursos/agregar', views.agregar_concurso, name="agregar_concurso"), # URL para agregar concursos
    path('concursos/<int:id_encuesta>/editar', views.modificar_concurso, name="modificar_concurso"), # URL para agregar concursos
    path('concursos/<int:id_encuesta>', views.ver_concursos, name="ver_concursos"), # URL para agregar concursos
    path('concursos/<int:id_encuesta>/eliminar', views.borrar_concurso, name="borrar_concurso"), # URL para agregar concursos
    path('encuestas', views.encuestas, name='encuestas'), # Página para ver las encuestas de las emisoras
    path('encuestas/<int:id_encuesta>', views.ver_encuesta, name="ver_encuesta"), # Página que muestra la informción de la encuesta
    path('encuestas/agregar', views.agregar_encuesta, name="agregar_encuesta"), # Página para ingresar una encuesta
    path('encuestas/<int:id_encuesta>/editar', views.modificar_encuesta, name="modificar_encuesta"), # Pagina para editar una encuesta
    path('encuestas/<int:id_encuesta>/eliminar', views.borrar_encuesta, name="borrar_encuesta"), # URL para eliminar la encuesta
]
