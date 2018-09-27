from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from WebAdminRadio.models import Emisora, Segmento

# Create your views here.

@login_required
def agregar_emisora(request):
    return render(request, 'webAdminRadio/agregar_emisora.html', {'title': 'Agregar Emisora'})

@login_required
def home(request):
    return render(request, 'webAdminRadio/index.html', {'title': 'Principal'})

@login_required
def segmentos(request):
    return render(request, 'webAdminRadio/segmento.html', {'title': 'Segmentos'})

@login_required
def agregar_segmento(request):
    emisoras = Emisora.objects.all()
    if request.POST:
        emisora = Emisora.objects.get(pk=request.POST['emisora'])
        nombre = request.POST['nombre']
        slogan = request.POST['slogan']
        descripcion = request.POST['descripcion']
        imagen = request.FILES['imagen']

        Segmento.objects.create(
            nombre=nombre,
            slogan=slogan,
            descripcion=descripcion,
            idEmisora=emisora,
            imagen=imagen
        )
        return redirect('webadminradio:segmentos')
    context = {'title': 'Agregar Segmento', 'emisoras': emisoras}
    return render(request, 'webAdminRadio/agregar_segmento.html', context)
