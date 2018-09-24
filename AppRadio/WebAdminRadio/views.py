from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'webAdminRadio/index.html', {'title': 'Principal'})
    return render(request, 'webAdminRadio/login.html', {'title': 'Login'})

@login_required
def agregar_emisora(request):
    return render(request,'webAdminRadio/agregar_emisora.html',{'title': 'Agregar Emisora'})

@login_required
def home(request):
    return render(request, 'webAdminRadio/index.html', {'title': 'Principal'})

@login_required
def agregar_segmento(request):
    return render(request, 'webAdminRadio/agregar_segmento.html', {'title': 'Agregar Segmento'})
