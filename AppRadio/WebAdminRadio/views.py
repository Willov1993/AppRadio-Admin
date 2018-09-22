from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'WebAdminRadio/login.html', {'title': 'Login'})

def agregar_segmento(request):
    return render(request, 'WebAdminRadio/agregar_segmento.html', {'title': 'Agregar Segmento'})