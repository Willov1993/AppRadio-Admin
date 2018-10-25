# api/urls.py
from django.urls import include, path
from .views import FacebookLogin,TwitterLogin,CreateUser
from . import views

urlpatterns = [
    path('emisoras/', views.ListEmisora.as_view()),
    path('segmentos/', views.ListSegmento.as_view()),
    path('segmentos/today',views.ListSegmentosDiaActual.as_view()),
    path('<int:id_emisora>/segmentos', views.ListEmisoraSegmento.as_view(), name="list_emisora_segmento"),
    path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('rest-auth/register/', CreateUser.as_view(), name='usuario_register'),
]