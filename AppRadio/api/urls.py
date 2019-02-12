# api/urls.py
from django.urls import include, path
from .views import FacebookLogin,TwitterLogin,CreateUser
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('hora_actual/',views.ListTime.as_view()),
    path('emisoras/', views.ListEmisora.as_view()),
    path('segmentos/', views.ListSegmento.as_view()),
    path('usuarios', views.ListUsuarios.as_view(), name="list_usuarios"),
    path('segmento/<int:id_segmento>/publicidad',views.ListPublicidad.as_view(), name="list_segmento_publicidad"),
    path('emisora/<int:id_emisora>/segmentos', views.ListEmisoraSegmentos.as_view(), name="list_emisora_segmentos"),
    path('emisora/<int:id_emisora>/segmento/<int:id_segmento>', views.ListEmisoraSegmento.as_view(), name="list_emisora_segmento"),
    path('segmento/<int:id_segmento>/locutores', views.ListLocutores.as_view(), name="list_segmento_locutor"),
    path('segmentos/today', views.ListSegmentosDiaActual.as_view()),
    path('emisoras/<int:id_emisora>/segmentos/today',views.ListSegmentosEmisoraDiaActual.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('rest-auth/register/', CreateUser.as_view(), name='usuario_register'),
    path('publicidad/<int:id_publicidad>/frecuencias', views.ListFrecuencias.as_view(), name='frecuencias'),
    path('emisoras/<int:id_emisora>/telefonos',views.ListTelefonosEmisora.as_view(),name='telefonos_emisora'),
    path('emisoras/<int:id_emisora>/redes_sociales',views.ListRedSocialEmisora.as_view(),name='redes_sociales_emisora'),
    path('segmentos/<int:id_segmento>/locutores',views.ListLocutoresSegmento.as_view(),name='locutores_segmento'),
    path('imagenes/', views.ListImagenes.as_view(), name="list_imagenes"),
    path('imagenes/<int:id_segmento>',views.ListImagenesSegmento.as_view(),name='imagenes_segmento'),
    path('videos/',views.ListVideos.as_view(),name="list_videos"),
    path('videos/<int:id_segmento>',views.ListVideosSegmento.as_view(),name='videos_segmento'),
    path('favoritos/<str:usuario>',views.ListFavoritosUsuario.as_view(),name='favoritos_usuario'),
    path('segmentos/<int:id_segmento>/encuestas', views.ListEncuestas.as_view(), name='encuestas'),
    path('favoritos_create/<int:id_segmento>/<str:username>', views.CreateFavoritoView, name='create_favorito'),

]