from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required
def home(request):
    return render(request, 'webAdminRadio/index.html', {'title': 'Principal'})

@login_required
def segmentos(request):
    list_segmentos = Segmento.objects.all()
    context = {'title': 'Segmentos', 'segmentos': list_segmentos}
    return render(request, 'webAdminRadio/segmentos.html', context)

@login_required
def emisoras(request):
    list_emisoras = Emisora.objects.all()
    context = {'title': 'Emisoras', 'emisoras': list_emisoras}
    return render(request, 'webAdminRadio/emisoras.html', context)

@login_required
def agregar_segmento(request):
    list_emisoras = Emisora.objects.all()
    context = {'title': 'Agregar Segmento', 'emisoras': list_emisoras}
    if request.POST:
        segmento_form = SegmentoForm(request.POST, request.FILES)
        if segmento_form.is_valid():
            segmento_form.save()
            # Iterar por todos los horarios
            for i in range(len(request.POST.getlist('dia'))):
                # Creación del horario
                Horario.objects.create(
                    dia=request.POST.getlist('dia')[i],
                    fecha_inicio=request.POST.getlist('inicio')[i],
                    fecha_fin=request.POST.getlist('fin')[i]
                )
                # Enlazar segmento con horario
                segmento_horario.objects.create(
                    idSegmento=Segmento.objects.order_by('-id')[0],
                    idHorario=Horario.objects.order_by('-id')[0]
                )
            context['success'] = '¡El registro del segmento se ha sido creado con éxito!'
        else:
            context['error'] = segmento_form.errors
        return render(request, 'webAdminRadio/agregar_segmento.html', context)
    return render(request, 'webAdminRadio/agregar_segmento.html', context)

@login_required
def agregar_emisora(request):
    """
    URL: webadmin/emisoras/agregar

    GET: muestra el formulario para agregar emisora
    POST: inserta una nueva emisora en la base de datos incluyendo telefonos y 
          redes sociales en caso de que se los hayan ingresado. 
    """
    if request.POST:
        #VALIDACIONES DEL FORM
        emisoraForm = EmisoraForm({
            'nombre':request.POST['nombre'],
            'frecuencia_dial': "{0} {1}".format(request.POST['frecuencia'],request.POST['tipoFrecuencia']),
            'url_streaming':request.POST['streaming'],
            'sitio_web':request.POST['sitioweb'],
            'direccion':request.POST['direccion'],
            'descripcion':request.POST['descripcion'],
            'ciudad': request.POST['ciudad'],
            'provincia': request.POST['provincia'],
            'logotipo': request.FILES['logo'],
        })

        if emisoraForm.is_valid() == False:
            for error in emisoraForm.errors:
                print('{0} -> {1}'.format(error,emisoraForm.errors[error]))
            context= {'title': 'Agregar Emisora','error':emisoraForm.errors}
            return render(request, 'webAdminRadio/agregar_emisora.html', context)
        
        dic_telefonos = {key:value for key, value in request.POST.items() if key.startswith("telefono")}
        
        for key, telefono in dic_telefonos.items():
            telForm= TelefonoForm({'telefono':telefono})
            if telForm.is_valid() == False:
                for error in telForm.errors:
                    print('{0} -> {1}'.format(error,telForm.errors[error]))
                context= {'title': 'Agregar Emisora','error':telForm.errors}
                return render(request, 'webAdminRadio/agregar_emisora.html', context)

        dic_redes = {key:value for key, value in request.POST.items() if key.startswith("red_social_url")}
        
        for key, url in dic_redes.items():
            if(url != ''):
                key= key.replace('url','nombre')
                nombre= request.POST[key]
                nombre= nombre[1] if isinstance(nombre,list) else nombre
                redForm= RedSocialForm({'nombre':nombre,'link':url})
                if redForm.is_valid() == False:
                    for error in redForm.errors:
                        print('{0} -> {1}'.format(error,redForm.errors[error]))
                    context= {'title': 'Agregar Emisora','error':redForm.errors}
                    return render(request, 'webAdminRadio/agregar_emisora.html', context)

        #CREACION DE REGISTRO
        try:
            emisora= Emisora(
                nombre= request.POST['nombre'],
                frecuencia_dial= "{0} {1}".format(request.POST['frecuencia'],request.POST['tipoFrecuencia']),
                url_streaming= request.POST['streaming'],
                sitio_web= request.POST['sitioweb'],
                direccion= request.POST['direccion'],
                descripcion= request.POST['descripcion'],
                ciudad= request.POST['ciudad'],
                provincia= request.POST['provincia'],
                logotipo= request.FILES['logo'],
            )
            emisora.save()

            dic_telefonos= sorted(dic_telefonos.items(),key= lambda t: t[0])
            for key,telefono in dic_telefonos:
                tel= Telefono_emisora(idEmisora=emisora,nro_telefono=telefono)
                tel.save()
            
            dic_redes= sorted(dic_redes.items(),key= lambda t: t[0])
            for key, url in dic_redes:
                if(url != ''):
                    key= key.replace('url','nombre')
                    nombre= request.POST[key]
                    nombre= nombre[1] if isinstance(nombre,list) else nombre
                    red= RedSocial_emisora(idEmisora=emisora,nombre=nombre,link=url)
                    red.save()
            
            context= {'title': 'Agregar Emisora', 'success':'¡El registro de la emisora se ha sido creado con éxito!'}
            return render(request, 'webAdminRadio/agregar_emisora.html', context)            

        except Exception as e:
            context = {
                'title': 'Agregar Emisora',
                'error':"""<p>Ocurrió un error al registrar los datos, intente nuevamente</p>
                    Error:<p>{0}</p>
                    Motivo: <p>{1!r}</p>
                """.format(type(e).__name__, e.args)
            }
            return render(request, 'webAdminRadio/agregar_emisora.html', context)

    return render(request, 'webAdminRadio/agregar_emisora.html', {'title': 'Agregar Emisora'})
