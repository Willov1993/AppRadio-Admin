from django.shortcuts import render
from WebAdminRadio.models import Segmento
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def agregar_emisora(request):
    if request.POST:
        #POST DATA
    else:
        return render(request,'webAdminRadio/agregar_emisora.html',{'title': 'Agregar Emisora'})

@login_required
def home(request):
    return render(request, 'webAdminRadio/index.html', {'title': 'Principal'})

@login_required
def agregar_segmento(request):

    if request.POST:
        print("POSTING DATA!")

    return render(request, 'webAdminRadio/agregar_segmento.html', {'title': 'Agregar Segmento'})
