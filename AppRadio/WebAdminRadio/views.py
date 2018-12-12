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
def agregar_emisora(request):
    context = {'title': 'Agregar Emisora'}
    if request.POST:
        emisora_form = EmisoraForm(request.POST, request.FILES)
        telefono = request.POST['telefono']
        redsocial= request.POST['red_social_url']
        telefono_form = TelefonoForm({'telefono': telefono})
        red_form = RedSocialForm({'red_social_url':redsocial})
        if (emisora_form.is_valid() and telefono_form.is_valid() and red_form.isvalid()):
            emisora_form.save()
            Telefono_emisora.objects.create(
                idEmisora=Emisora.objects.order_by('-id')[0],
                nro_telefono = telefono
                )
            RedSocial_emisora.objects.create(
                idEmisora = Emisora.objects.order_by('-id')[0],
                nombre= Emisora.objects.getlist('red_social_nombre'),
                link=redsocial
                )
        else:   
            context['error'] = emisora_form.errors
        if 'error' not in context:
            context['success'] = '¡El registro de la emisora ha sido creado con éxito!'
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
def agregar_publicidad(request):
    list_emisoras = Emisora.objects.filter(activo='A')
    context = {'title': 'Agregar Publicidad', 'emisoras': list_emisoras}
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
    return render(request, 'webAdminRadio/agregar_publicidad.html', context)



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
    edit_emisora = Emisora.objects.get(id=id_emisora)
    context = {
        'title': 'Editar Emisora',
        'emisora': edit_emisora,
    }
    if request.POST:
        emisora_form = EmisoraForm(request.POST, request.FILES, edit_emisora)
        if emisora_form.is_valid():
            emisora_form.save()
            if 'error' not in context:
                context['success'] = '¡El registro del segmento se ha sido creado con éxito!'            
        else:
            context['error'] = emisora_form.errors
        return render(request, 'webAdminRadio/modificar_emisora.html', context)
    return render(request, 'webAdminRadio/modificar_emisora.html', context)

@login_required
def locutores(request):
    list_segmentos = Segmento.objects.filter(activo='A')
    context = {
        'title': 'Locutores',
        'segmentos': list_segmentos
    }
    return render(request, 'webAdminRadio/locutores.html', context)

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
    if request.POST:
        segmento_form = SegmentoForm(request.POST, request.FILES, instance=edit_segmento)
        if segmento_form.is_valid():
            segmento_form.save()
            # Iterar por todos los horarios
            for i in range(len(request.POST.getlist('dia'))):
                dia = request.POST.getlist('dia')[i]
                horario_form = HorarioForm({
                    'dia': request.POST.getlist('dia')[i],
                    'inicio': request.POST.getlist('inicio')[i],
                    'fin': request.POST.getlist('fin')[i]
                })
                if horario_form.is_valid():
                    # Falta implementar
                    horario, created = Horario.objects.get(dia=dia)
                    if created:
                        segmento_horario.objects.create(
                            idSegment=Segmento.objects.order_by('-id')[0],
                            idHorario=Horario.objects.order_by('-id')[0]
                        )
                    else:
                        horario.fecha_inicio = request.POST.getlist('inicio')[i]
                        horario.fecha_fin = request.POST.getlist('fin')[i]

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

