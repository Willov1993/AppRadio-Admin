# api/urls.py
from django.urls import include, path
from .views import FacebookLogin,TwitterLogin
from . import views

urlpatterns = [
    path('emisoras/', views.ListEmisora.as_view()),
    path('segmentos/', views.ListSegmento.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
]