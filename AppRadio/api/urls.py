# api/urls.py
from django.urls import include, path
from .views import FacebookLogin,TwitterLogin,CreateUser
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
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
]