from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Login del usuario
def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('webadminradio:home')
            else:
                messages.error(request, 'Esta cuenta ha sido desactivada')
                return redirect('accounts:login')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrecto')
            return redirect('accounts:login')
    return render(request, 'accounts/login.html', {'title': 'Login'})

# Logout del usuario
def logout_user(request):
    if request.POST:
        logout(request)
        return redirect('accounts:login')