from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_user, name='login'), # URL para hacer login del usuario
    path('logout/', views.logout_user, name='logout'), # URL para hacer logout del usuario
]