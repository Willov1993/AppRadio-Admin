from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_user, name='login'), # URL para hacer login del usuario
    path('logout/', views.logout_user, name='logout'), # URL para hacer logout del usuario
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]