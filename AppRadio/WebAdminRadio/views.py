from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from accounts.models import Usuario

# Create your views here.

@login_required
def home(request):
    return render(request, 'webAdminRadio/index.html', {'title': 'Principal'})

@login_required
def segmentos(request):
    list_emisoras = Emisora.objects.all()
    context = {'title': 'Segmentos', 'emisoras': list_emisoras}
    return render(request, 'webAdminRadio/segmentos.html', context)

@login_required
def emisoras(request):
    list_emisoras = Emisora.objects.all()
    context = {'title': 'Emisoras', 'emisoras': list_emisoras}
    return render(request, 'webAdminRadio/emisoras.html', context)

@login_required
def publicidad(request):
    list_emisoras = Emisora.objects.all()
    context = {'title': 'Publicidad', 'emisoras': list_emisoras}
    return render(request, 'webAdminRadio/publicidad.html', context)

@login_required
def agregar_segmento(request):
    list_emisoras = Emisora.objects.all()
    context = {'title': 'Agregar Segmento', 'emisoras': list_emisoras}
    if request.POST:
        segmento_form = SegmentoForm(request.POST, request.FILES)
        if segmento_form.is_valid():
            # Iterar por todos los horarios
            for i in range(len(request.POST.getlist('dia'))):
                print(request.POST.getlist('inicio')[i])
                print(request.POST.getlist('fin')[i])
                # Creación del horario
                horario_form = HorarioForm({
                    'dia': request.POST.getlist('dia')[i],
                    'inicio': request.POST.getlist('inicio')[i],
                    'fin': request.POST.getlist('fin')[i]
                })
                if horario_form.is_valid():
                    segmento_form.save()
                    horario_form.save()
                    # Enlazar segmento con horario
                    segmento_horario.objects.create(
                        idSegmento=Segmento.objects.order_by('-id')[0],
                        idHorario=Horario.objects.order_by('-id')[0]
                    )
                else:
                    context['error'] = horario_form.errors
                    break
            if 'error' not in context:
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

@login_required
def agregar_publicidad(request):
    list_emisoras = Emisora.objects.all()
    context = {'title': 'Agregar Publicidad', 'emisoras': list_emisoras}
    if request.POST:
        segmento_form = SegmentoForm(request.POST, request.FILES)
        if segmento_form.is_valid():
            segmento_form.save()
            # Iterar por todos los horarios
            for i in range(len(request.POST.getlist('dia'))):
                # Creación del horario
                horario_form = HorarioForm(request.POST)
                if horario_form.is_valid():
                    horario_form.save()
                    # Enlazar segmento con horario
                    segmento_horario.objects.create(
                        idSegmento=Segmento.objects.order_by('-id')[0],
                        idHorario=Horario.objects.order_by('-id')[0]
                    )
                else:
                    context['error'] = horario_form.errors
                    break
            if 'error' not in context:
                context['success'] = '¡El registro del segmento se ha sido creado con éxito!'
        else:
            context['error'] = segmento_form.errors
        return render(request, 'webAdminRadio/agregar_segmento.html', context)
    return render(request, 'webAdminRadio/agregar_segmento.html', context)


@login_required
def ver_segmento(request, id_segmento):
    segmento = Segmento.objects.get(id=id_segmento)
    context = {
        'title': 'Información del segmento',
        'segmento': segmento
    }
    return render(request, 'webAdminRadio/ver_segmento.html', context)

@login_required
def modificar_segmento(request, id_segmento):
    segmento = Segmento.objects.get(id=id_segmento)
    list_emisoras = Emisora.objects.all()
    if request.POST:
        print("Aquí va el form")
    context = {
        'title': 'Editar Segmento',
        'segmento': segmento,
        'emisoras': list_emisoras
    }
    return render(request, 'webAdminRadio/editar_segmento.html', context)

@login_required
def modificar_emisora(request, id_emisora):
    emisora = Emisora.objects.get(id=id_emisora)
    if request.POST:
        print("Aquí va el form")
    context = {
        'title': 'Editar Emisora',
        'emisora': emisora
        }
    return render(request, 'webAdminRadio/modificar_emisora.html', context)

@login_required
def locutores(request):
    list_segmentos = Segmento.objects.all()
    context = {
        'title': 'Locutores',
        'segmentos': list_segmentos
    }
    return render(request, 'webAdminRadio/locutores.html', context)

@login_required
def agregar_locutor(request):
    list_emisoras = Emisora.objects.all()
    context = {'title': 'Agregar Locutores', 'emisoras': list_emisoras}
    if request.POST:
        usuario_form = UsuarioForm(request.POST, request.FILES, {'rol':'1'})
        telf = request.POST['telefono']
        telefono_form = TelefonoForm({'telefono': telf})
        if (usuario_form.is_valid() and telefono_form.is_valid()):
            usuario_form.save()
            new_locutor = Usuario.objects.order_by('-id')[0]
            Telefono_Usuario.objects.create(
                idUsuario=new_locutor,
                nro_telefono=telf
            )
            print(request.POST)
            for s in request.POST.getlist('segmento'):
                segmento_usuario.objects.create(
                    idUsuario=new_locutor,
                    idSegmento=Segmento.objects.get(id=s)
                )
        else:
            if telefono_form.has_error:
                context['error'] = telefono_form.errors
            if usuario_form.has_error:
                context['error'] = usuario_form.errors
            return render(request, 'webAdminRadio/agregar_locutor.html', context)
        context['success'] = '¡El registro del locutor se ha sido creado con éxito!'
    return render(request, 'webAdminRadio/agregar_locutor.html', context)

@login_required
def ver_locutor(request, id_locutor):
    segmentos = segmento_usuario.objects.filter(idUsuario=id_locutor)
    locutor = Usuario.objects.get(id=id_locutor)
    telefono = Telefono_Usuario.objects.get(idUsuario=locutor)
    context = {
        'title': "Informacion del locutor",
        'locutor': locutor,
        'telefono': telefono,
        'segmentos': segmentos
    }
    return render(request, 'webAdminRadio/ver_locutor.html', context)