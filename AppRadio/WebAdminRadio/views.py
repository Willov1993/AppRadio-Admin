from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'webAdminRadio/login.html', {'title': 'Login'})

def agregar_emisora(request):
    return render(request,'webAdminRadio/agregar_emisora.html',{'title': 'Agregar Emisora'})

def agregar_segmento(request):
    return render(request, 'webAdminRadio/agregar_segmento.html', {'title': 'Agregar Segmento'})
