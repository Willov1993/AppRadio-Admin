import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from accounts.models import Usuario
from .models import *
from .forms import *

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
    list_emisoras = Emisora.objects.filter(activo='A')
    context = {'title': 'Emisoras', 'emisoras': list_emisoras}
    return render(request, 'webAdminRadio/emisoras.html', context)

@login_required
def publicidad(request):
    publicidad = Publicidad.objects.filter(estado='A')

    list_segmentos = Segmento.objects.filter(activo='A')
    context = {
        'title': 'Publicidad',
        'segmentos': list_segmentos,
        'publicidad':publicidad
    }
    return render(request, 'webAdminRadio/publicidad.html', context)

@login_required
def locutores(request):
    list_segmentos = Segmento.objects.filter(activo='A')
    emisoras = Emisora.objects.filter(activo='A')
    context = {
        'title': 'Locutores',
        'segmentos': list_segmentos,
        'emisoras': emisoras
    }
    return render(request, 'webAdminRadio/locutores.html', context)

@login_required
def encuestas(request):
    emisoras = Emisora.objects.filter(activo='A')
    context = {
        'title': "Encuestas",
        'emisoras': emisoras
    }
    return render(request, 'webAdminRadio/encuestas.html', context)

@login_required
def agregar_emisora(request):
    context = {'title': 'Agregar Emisora'}
    if request.POST:
        emisora_form = EmisoraForm(request.POST, request.FILES)
        if not emisora_form.is_valid():
            context['error'] = emisora_form.errors
            return render(request, 'webAdminRadio/agregar_emisora.html', context)

        for i in range(len(request.POST.getlist('telefono'))):
            telefono_form = TelefonoForm({
                'telefono':request.POST.getlist('telefono')[i]
            })
            if not telefono_form.is_valid():
                context['error'] = telefono_form.errors
                return render(request, 'webAdminRadio/agregar_emisora.html', context)

        for i in range(len(request.POST.getlist('red_social_nombre'))):
            red_form = RedSocialForm({
                'nombre': request.POST.getlist('red_social_nombre')[i],
                'link': request.POST.getlist('red_social_url')[i]
            })
            if not red_form.is_valid():
                context['error'] = red_form.errors
                return render(request, 'webAdminRadio/agregar_emisora.html', context)

        emisora_form.save()
        for i in range(len(request.POST.getlist('telefono'))):
            Telefono_emisora.objects.create(
                idEmisora=Emisora.objects.order_by('-id')[0],
                nro_telefono=request.POST.getlist('telefono')[i]
            )
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            RedSocial_emisora.objects.create(
                idEmisora=Emisora.objects.order_by('-id')[0],
                nombre=request.POST.getlist('red_social_nombre')[i],
                link=request.POST.getlist('red_social_url')[i]
            )
        context['success'] = '¡La emisora ha sido registrada con éxito!'
        return render(request, 'webAdminRadio/agregar_emisora.html', context)
    return render(request, 'webAdminRadio/agregar_emisora.html', context)

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
                horario_form = HorarioForm({
                    'dia': request.POST.getlist('dia')[i],
                    'inicio': request.POST.getlist('inicio')[i],
                    'fin': request.POST.getlist('fin')[i]
                })
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
def agregar_concurso(request):
    list_usuarios = Usuario.objects.all()
    list_emisoras = Emisora.objects.filter(activo='A')
    list_segmentos = Segmento.objects.filter(activo='A')
    context ={
        'title': 'Agregar Concurso',
        'usuarios': list_usuarios,
        'emisoras': list_emisoras,
        'segmentos': list_segmentos
        }
    return render(request, 'webAdminRadio/agregar_concurso.html', context)


@login_required
def agregar_publicidad(request):
    list_emisoras = Emisora.objects.filter(activo='A')
    context = {
        'title': 'Agregar Publicidad',
        'emisoras': list_emisoras
        }
    if request.POST:
        publicidad_form = PublicidadForm(request.POST, request.FILES)
        if publicidad_form.is_valid():
            publicidad_form.save()
            # Iterar por todos los horarios
            for i in range(len(request.POST.getlist('tipo'))):
                frecuencia_form = FrecuenciaForm({
                    'tipo': request.POST.getlist('tipo')[i],
                    'dia': request.POST.getlist('dia_semana')[i],
                    'inicio': request.POST.getlist('hora_inicio')[i],
                    'fin': request.POST.getlist('hora_fin')[i]
                })
                if frecuencia_form.is_valid():
                    frecuencia_form.save()
                    frecuencia_publicidad.objects.create(
                        idPublicidad=Publicidad.objects.order_by('-id')[0],
                        idFrecuencia=Frecuencia.objects.order_by('-id')[0]
                    )
                else:
                    context['error'] = frecuencia_form.errors
                    break
            for s in request.POST.getlist('segmento'):
                segmento_publicidad.objects.create(
                    idPublicidad=Publicidad.objects.order_by('-id')[0],
                    idSegmento=Segmento.objects.get(id=s)
                )
            if 'error' not in context:
                context['success'] = '¡El registro de la publicidad se ha sido creado con éxito!'
        else:
            context['error'] = publicidad_form.errors
    return render(request, 'webAdminRadio/agregar_publicidad.html', context)

@login_required
def agregar_encuesta(request):
    emisoras = Emisora.objects.filter(activo='A')
    '''
    if request.POST:
        encuesta_form = EncuestaFrom(request.POST)
        if encuesta_form.is_valid():
            new_encuesta = encuesta_form.save()
            for i in range(len(request.POST.getlist('pregunta'))):
                pregunta_form = PreguntaForm({
                    'contenido': request.POST.getlist('pregunta')[i],
                    'idEncuesta': new_encuesta
                })
                if pregunta_form.is_valid():
                    pregunta_form.save()
            for i in range(len(request.POST.getlist('respuesta'))):
                respuesta_form = RespuestaForm({
                    ''
                })
    '''
    context = {
        'title': "Agregar Encuesta",
        'emisoras': emisoras,
    }
    return render(request, 'webAdminRadio/agregar_encuesta.html', context)

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
    edit_segmento = Segmento.objects.get(id=id_segmento, activo='A')
    horarios = Horario.objects.filter(pk__in=segmento_horario.objects.filter(idSegmento=edit_segmento))
    list_emisoras = Emisora.objects.all()
    context = {
        'title': 'Editar Segmento',
        'segmento': edit_segmento,
        'emisoras': list_emisoras,
        'horarios': json.dumps(list(horarios.values('dia', 'fecha_inicio', 'fecha_fin')), cls=DjangoJSONEncoder)
    }
    if request.POST:
        segmento_form = SegmentoForm(request.POST, request.FILES, instance=edit_segmento)
        if segmento_form.is_valid():
            segmento_form.save()
            horarios.delete()
            for i in range(len(request.POST.getlist('dia'))):
                horario_form = HorarioForm({
                    'dia': request.POST.getlist('dia')[i],
                    'inicio': request.POST.getlist('inicio')[i],
                    'fin': request.POST.getlist('fin')[i]
                })
                if horario_form.is_valid():
                    horario_form.save()
                    segmento_horario.objects.create(
                        idSegmento=edit_segmento,
                        idHorario=Horario.objects.order_by('-id')[0]
                    )
                else:
                    context['error'] = horario_form.errors
                    break
                context['success'] = '¡El registro ha sido modificado con éxito!'
        else:
            context['error'] = segmento_form.errors
        return render(request, 'webAdminRadio/editar_segmento.html', context)
    return render(request, 'webAdminRadio/editar_segmento.html', context)

@login_required
def modificar_emisora(request, id_emisora):
    edit_emisora = Emisora.objects.get(id=id_emisora, activo='A')
    red_social = RedSocial_emisora.objects.filter(idEmisora=id_emisora)
    telefono_emisora = Telefono_emisora.objects.filter(idEmisora=id_emisora)
    context = {
        'title': 'Editar Emisora',
        'emisora': edit_emisora,
        'telefono': telefono_emisora,
        'redsocial': red_social
    }
    if request.POST:
        emisora_form = EmisoraForm(request.POST, request.FILES, instance=edit_emisora)
        if not emisora_form.is_valid():
            context['error'] = emisora_form.errors
            return render(request, 'webAdminRadio/modificar_emisora.html', context)

        for i in range(len(request.POST.getlist('telefono'))):
            telefono_form = TelefonoForm({
                'telefono': request.POST.getlist('telefono')[i]
            })
            if not telefono_form.is_valid():
                context['error'] = telefono_form.errors
                return render(request, 'webAdminRadio/modificar_emisora.html', context)

        for i in range(len(request.POST.getlist('red_social_nombre'))):
            red_form = RedSocialForm({
                'nombre': request.POST.getlist('red_social_nombre')[i],
                'link': request.POST.getlist('red_social_url')[i]
            })
            if not red_form.is_valid():
                context['error'] = red_form.errors
                return render(request, 'webAdminRadio/modificar_emisora.html', context)

        emisora_form.save()
        telefono_emisora.delete()
        red_social.delete()
        for i in range(len(request.POST.getlist('telefono'))):
            Telefono_emisora.objects.create(
                idEmisora=edit_emisora,
                nro_telefono=request.POST.getlist('telefono')[i]
            )
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            RedSocial_emisora.objects.create(
                idEmisora=edit_emisora,
                nombre=request.POST.getlist('red_social_nombre')[i],
                link=request.POST.getlist('red_social_url')[i]
            )

        context['success'] = "¡La emisora ha sido registrada con éxito!"
        return render(request, 'webAdminRadio/modificar_emisora.html', context)
    return render(request, 'webAdminRadio/modificar_emisora.html', context)

@login_required
def asignar_locutor(request):
    list_emisoras = Emisora.objects.all()
    context = {
        'title': 'Asignar Locutor',
        'emisoras': list_emisoras
    }
    return render(request, 'webAdminRadio/asignar_locutor.html', context)

@login_required
def ver_locutor(request, id_locutor):
    edit_segmento = segmento_usuario.objects.filter(idUsuario=id_locutor)
    locutor = Usuario.objects.get(id=id_locutor)
    telefono = Telefono_Usuario.objects.get(idUsuario=locutor)
    context = {
        'title': "Informacion del locutor",
        'locutor': locutor,
        'telefono': telefono,
        'segmentos': edit_segmento
    }
    return render(request, 'webAdminRadio/ver_locutor.html', context)


@login_required
def ver_publicidad(request, id_publicidad):
    publicidad = Publicidad.objects.get(id=id_publicidad)
    segmento = segmento_publicidad.objects.filter(idPublicidad=id_publicidad)
    frecuencia = frecuencia_publicidad.objects.filter(idPublicidad=id_publicidad)
    context = {
        'title': "Informacion de la publicidad",
        'publicidad':publicidad,
        'segmentos': segmento,
        'horarios': frecuencia
    }
    return render(request, 'webAdminRadio/ver_publicidad.html', context)

@login_required
def modificar_locutor(request, id_locutor):
    list_emisoras = Emisora.objects.all()
    edit_locutor = Usuario.objects.get(id=id_locutor)
    list_segmentos = Segmento.objects.filter(pk__in=segmento_usuario.objects.filter(idUsuario=edit_locutor), activo='A')
    edit_telef = Telefono_Usuario.objects.get(idUsuario=id_locutor)
    segmentos_loc = segmento_usuario.objects.filter(idUsuario=id_locutor)
    context = {
        'title': 'Editar Locutor',
        'locutor': edit_locutor,
        'telefono': edit_telef,
        'emisoras': list_emisoras,
        'segmentos': json.dumps(list(list_segmentos.values('id', 'nombre')), cls=DjangoJSONEncoder)
    }
    if request.POST:
        usuario_form = UsuarioForm(request.POST, request.FILES, instance=edit_locutor)
        telf = request.POST['telefono']
        telefono_form = TelefonoForm({'telefono': telf}, instance=edit_telef)
        if (usuario_form.is_valid() and telefono_form.is_valid()):
            usuario_form.save()
            telefono_form.save()
            segmentos_loc.delete()
            for s in request.POST.getlist('segmento'):
                segmento_usuario.objects.create(
                    idUsuario=edit_locutor,
                    idSegmento=Segmento.objects.get(id=s)
                )
        else:
            if telefono_form.has_error:
                context['error'] = telefono_form.errors
            if usuario_form.has_error:
                context['error'] = usuario_form.errors
            return render(request, 'webAdminRadio/editar_locutor.html', context)
        context['success'] = '¡El registro del locutor se ha sido creado con éxito!'
    return render(request, 'webAdminRadio/editar_locutor.html', context)

@login_required
def asignar_locutor_segmento(request, id_locutor, id_segmento):
    new_locutor = Usuario.objects.get(id=id_locutor)
    segmento = Segmento.objects.get(id=id_segmento)
    new_locutor.rol = 'L'
    new_locutor.save()
    segmento_usuario.objects.create(
        idSegmento=segmento,
        idUsuario=new_locutor
    )
    messages.success(request, 'El usuario ha sido asignado como locutor')
    return redirect('webadminradio:asignar_locutor')

@login_required
def modificar_publicidad(request, id_publicidad):
    edit_publicidad = Publicidad.objects.get(id=id_publicidad)
    horarios = Frecuencia.objects.filter(pk__in=frecuencia_publicidad.objects.filter(idPublicidad=edit_publicidad))
    list_emisoras = Emisora.objects.all()
    list_segmentos = Segmento.objects.filter(pk__in=segmento_publicidad.objects.filter(idPublicidad=edit_publicidad).values('idSegmento'))
    list_segmentos_publicidad = segmento_publicidad.objects.filter(idPublicidad=edit_publicidad)
    context = {
        'title': 'Editar Publicidad',
        'publicidad': edit_publicidad,
        'emisoras': list_emisoras,
        'horarios': json.dumps(list(horarios.values('tipo','dia_semana', 'hora_inicio', 'hora_fin')), cls=DjangoJSONEncoder),
        'segmentos': json.dumps(list(list_segmentos.values('id', 'nombre')), cls=DjangoJSONEncoder)
    }
    if request.POST:
        publicidad_form = PublicidadForm(request.POST, request.FILES, instance=edit_publicidad)
        if publicidad_form.is_valid():
            publicidad_form.save()
            horarios.delete()
            list_segmentos_publicidad.delete()
            for i in range(len(request.POST.getlist('dia'))):
                frecuencia_form = FrecuenciaForm({
                    'tipo': request.POST.getlist('tipo')[i],
                    'dia': request.POST.getlist('dia')[i],
                    'inicio': request.POST.getlist('inicio')[i],
                    'fin': request.POST.getlist('fin')[i]
                })
                if frecuencia_form.is_valid():
                    frecuencia_form.save()
                    frecuencia_publicidad.objects.create(
                        idPublicidad=edit_publicidad,
                        idFrecuencia=Frecuencia.objects.order_by('-id')[0]
                    )
                else:
                    context['error'] = frecuencia_form.errors
                    break
            for s in request.POST.getlist('segmento'):
                segmento_publicidad.objects.create(
                    idPublicidad=edit_publicidad,
                    idSegmento=Segmento.objects.get(id=s)
                )
            if 'error' not in context:
                context['success'] = '¡El registro ha sido modificado con éxito!'
        else:
            context['error'] = publicidad_form.errors
        return render(request, 'webAdminRadio/editar_publicidad.html', context)
    return render(request, 'webAdminRadio/editar_publicidad.html', context)

@login_required
def agregar_usuario(request):
    context = {'title': 'Agregar Usuario'}
    if request.POST:
        nombre = request.POST['nombre']
        apellidos = request.POST['apellido']
        username = nombre[0].lower() + apellidos.partition(' ')[0].lower()
        password = Usuario.objects.make_random_password()
        user_form = UsuarioForm({
            'nombre': nombre,
            'apellido': apellidos,
            'username': username,
            'password': password,
            'email': request.POST['email'],
            'fechaNac': request.POST['fechaNac'],
            'rol': request.POST['tipo_select'],
            'apodo': request.POST['apodo'],
            'biografia': request.POST['biografia'],
            'hobbies': request.POST['hobbies']
        })

        telefono_form = TelefonoForm({
            'telefono': request.POST['telefono']
        })

        if not telefono_form.is_valid():
            context['error'] = telefono_form.errors
            return render(request, 'webAdminRadio/agregar_usuario.html', context)

        for i in range(len(request.POST.getlist('red_social_nombre'))):
            red_social_form = RedSocialForm({
                'nombre': request.POST.getlist('red_social_nombre')[i],
                'link': request.POST.getlist('red_social_url')[i]
            })
            if not red_social_form.is_valid():
                context['error'] = red_social_form.errors
                return render(request, 'webAdminRadio/agregar_usuario.html', context)

        if user_form.is_valid():
            user_form.save()
            Telefono_Usuario.objects.create(
                idUsuario=Usuario.objects.order_by('-id')[0],
                nro_telefono=request.POST['telefono']
            )
            for i in range(len(request.POST.getlist('red_social_nombre'))):
                RedSocial_usuario.objects.create(
                    idUsuario=Usuario.objects.order_by('-id')[0],
                    nombre=request.POST.getlist('red_social_nombre')[i],
                    link=request.POST.getlist('red_social_url')[i]
                )
            context['success'] = '¡El usuario ha sido registrado!'
        else:
            context['error'] = user_form.errors
    return render(request, 'webAdminRadio/agregar_usuario.html', context)

@login_required
def modificar_usuario(request, id_usuario):
    edit_usuario = Usuario.objects.get(id=id_usuario)
    edit_telefono = Telefono_Usuario.objects.get(idUsuario=id_usuario)
    redes = RedSocial_usuario.objects.filter(idUsuario=id_usuario)
    context = {
        'title': 'Editar Usuario',
        'usuario': edit_usuario,
        'telefono': edit_telefono
    }
    if request.POST:
        nombre = request.POST['nombre']
        apellidos = request.POST['apellido']
        username = nombre[0].lower() + apellidos.partition(' ')[0].lower()
        password = Usuario.objects.make_random_password()
        user_form = UsuarioForm({
            'nombre': nombre,
            'apellido': apellidos,
            'username': username,
            'password': password,
            'email': request.POST['email'],
            'fechaNac': request.POST['fechaNac'],
            'rol': request.POST['tipo_select'],
            'apodo': request.POST['apodo'],
            'biografia': request.POST['biografia'],
            'hobbies': request.POST['hobbies']
        }, instance=edit_usuario)

        telefono_form = TelefonoForm({
            'telefono': request.POST['telefono']
        })

        if not telefono_form.is_valid():
            context['error'] = telefono_form.errors
            return render(request, 'webAdminRadio/editar_usuario.html', context)

        for i in range(len(request.POST.getlist('red_social_nombre'))):
            red_social_form = RedSocialForm({
                'nombre': request.POST.getlist('red_social_nombre')[i],
                'link': request.POST.getlist('red_social_url')[i]
            })
            if not red_social_form.is_valid():
                context['error'] = red_social_form.errors
                return render(request, 'webAdminRadio/editar_usuario.html', context)

        if user_form.is_valid():
            user_form.save()
            edit_telefono.nro_telefono = request.POST['telefono']
            redes.delete()
            for i in range(len(request.POST.getlist('red_social_nombre'))):
                RedSocial_usuario.objects.create(
                    idUsuario=edit_usuario,
                    nombre=request.POST.getlist('red_social_nombre')[i],
                    link=request.POST.getlist('red_social_url')[i]
                )
            context['success'] = '¡El usuario ha sido modificado exitosamente!'
        else:
            context['error'] = user_form.errors
    return render(request, 'webAdminRadio/editar_usuario.html', context)

@login_required
def ver_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    telefono = Telefono_Usuario.objects.get(idUsuario=id_usuario)
    redes = RedSocial_usuario.objects.filter(idUsuario=id_usuario)
    context = {
        'title': 'Información del Usuario',
        'usuario': usuario,
        'telefono': telefono,
        'redes': redes
    }
    return render(request, 'webAdminRadio/ver_usuario.html', context)

@login_required
def sugerencias(request):
    list_sugerencias = Sugerencia.objects.all().order_by("-fecha_creacion")
    query = request.GET.get("q")
    if query:
        try:
            list_sugerencias = list_sugerencias.filter(Q(fecha_creacion__year=query))
        except ValueError:
            list_sugerencias = list_sugerencias.filter(
                Q(mensaje__icontains=query) |
                Q(idUsuario__first_name__icontains=query) |
                Q(idUsuario__last_name__icontains=query) |
                Q(idSegmento__nombre__icontains=query) |
                Q(idEmisora__nombre__icontains=query)
            ).distinct()
    paginator = Paginator(list_sugerencias, 2)
    page = request.GET.get('page')
    list_sugerencias = paginator.get_page(page)
    context = {'title': 'Sugerencias', 'sugerencias': list_sugerencias}
    return render(request, 'webAdminRadio/sugerencias.html', context)

@login_required
def usuarios(request):
    context = {'title': 'Usuarios'}
    return render(request, 'webAdminRadio/usuarios.html', context)

@login_required
def borrar_emisora(request, id_emisora):
    delete_segmento = Emisora.objects.get(id=id_emisora)
    delete_segmento.activo = 'I'
    delete_segmento.save()
    messages.success(request, 'La emisora ha sido eliminada')
    return redirect('webadminradio:emisoras')

@login_required
def borrar_segmento(request, id_segmento):
    delete_segmento = Segmento.objects.get(id=id_segmento)
    delete_segmento.activo = 'I'
    delete_segmento.save()
    messages.success(request, 'El segmento ha sido eliminado')
    return redirect('webadminradio:segmentos')

@login_required
def borrar_publicidad(request, id_publicidad):
    delete_publicidad = Publicidad.objects.get(id=id_publicidad)
    delete_publicidad.estado = 'I'
    delete_publicidad.save()
    messages.success(request, 'La publicidad ha sido eliminada con exito')
    return redirect('webadminradio:publicidad')

@login_required
def borrar_locutor(request, id_locutor):
    delete_locutor = Usuario.objects.get(id=id_locutor)
    delete_locutor.is_active = False
    delete_locutor.save()
    messages.success(request, 'El locutor ha sido eliminado')
    return redirect('webadminradio:locutores')

@login_required
def borrar_usuario(request, id_usuario):
    delete_usuario = Usuario.objects.get(id=id_usuario)
    delete_usuario.is_active = False
    delete_usuario.save()
    messages.success(request, 'El usuario ha sido eliminado')
    return redirect('webadminradio:usuarios')
