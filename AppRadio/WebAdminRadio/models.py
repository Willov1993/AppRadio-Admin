from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core import serializers
from accounts.models import Usuario
from datetime import datetime

DIAS=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

def emisora_file_location(instance, filename):
    #Esta función guarda las imagenes de las emisoras en la ruta:
    # media_cdn/<emisora.slug>
    return "%s/%s" %(instance.slug, filename)

def segmento_file_location(instance, filename):
    # Esta función guarda las imágenes de los segmentos en la ruta:
    # media_cdn/<emisora.slug>/<segmento.slug>
    return "%s/%s/%s" %(instance.idEmisora.slug, instance.slug, filename)

def upload_location(instance, filename):
    #Esta función guarda las imágenes de los usuarios en media_cdn/<id_usuario>
    return "usuarios/%s/%s" %(instance.id, filename)

"""class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nac = models.DateField()
    imagen = models.ImageField(upload_to=upload_location, blank=True)
    rol = models.CharField(max_length=1)"""


class Emisora(models.Model):
    #idEmisora = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    frecuencia_dial = models.CharField(max_length=8)
    url_streaming = models.CharField(max_length=150)
    sitio_web = models.CharField(max_length=150, null=True, blank=True)
    direccion = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    logotipo = models.ImageField(upload_to=emisora_file_location)
    activo = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.nombre

class Segmento(models.Model):
    #idSegmento = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    slogan = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=250)
    idEmisora = models.ForeignKey(Emisora, on_delete=models.DO_NOTHING)
    imagen = models.ImageField(upload_to=segmento_file_location)
    activo = models.CharField(max_length=1, default='A')

    # Esta función retorna todos los horarios del segmento
    def get_horarios(self):
        return Horario.objects.filter(pk__in=segmento_horario.objects.filter(idSegmento=self.pk)).values('dia', 'fecha_inicio', 'fecha_fin')

    def get_horario_dia_actual(self):
        day= datetime.now().weekday()
        dia_actual= DIAS[day]
        horarios= Horario.objects.filter(pk__in=segmento_horario.objects.filter(idSegmento=self.pk))
        return horarios.filter(dia=dia_actual).values('dia', 'fecha_inicio', 'fecha_fin').order_by('fecha_inicio')

    def get_emisora(self):
        return self.idEmisora

    def __str__(self):
        return self.nombre

class Encuesta(models.Model):
    #idEncuesta = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 150)
    descripcion = models.CharField(max_length = 250)
    imagen = models.CharField(max_length = 250)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    activo = models.CharField(max_length = 1, default='A')

class Horario(models.Model):
    #idHorario = models.AutoField(primary_key = True)
    dia = models.CharField(max_length=9)
    fecha_inicio = models.TimeField()
    fecha_fin = models.TimeField()
    activo = models.CharField(max_length = 1, default='A')

    def __str__(self):
        return self.dia + " [" + str(self.fecha_inicio) + " - " + str(self.fecha_fin) + "]"

class Publicidad(models.Model):
    titulo = models.CharField(max_length = 150)
    cliente = models.CharField(max_length = 80)
    descripcion = models.CharField(max_length = 350)
    url = models.CharField(max_length = 150)
    estado = models.CharField(max_length = 1, default='A')
    imagen = models.ImageField(upload_to = upload_location, blank=None)

    def __str__(self):
        return self.titulo

class Tipo_sugerencia(models.Model):
    nombre = models.CharField(max_length = 15)
    descripcion = models.CharField(max_length = 500)

    def __str__(self):
        return self.nombre

class Sugerencia(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    mensaje = models.CharField(max_length=250)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    idEmisora = models.ForeignKey(Emisora, on_delete=models.DO_NOTHING)
    idSegmento = models.ForeignKey(Segmento, on_delete=models.DO_NOTHING, null=True, blank=True)
    idTipo = models.ForeignKey(Tipo_sugerencia, on_delete=models.DO_NOTHING)
    activo = models.CharField(max_length=1, default='A')

    def __str__(self):
        return str(self.idUsuario) + " : " + str(self.idTipo)

class Frecuencia(models.Model):
    tipo = models.CharField(max_length = 8)
    dia_semana = models.CharField(max_length = 9, blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null = True)
    activo = models.CharField(max_length = 1, default='A')

    def __str__(self):
        return self.tipo +" "+ self.dia_semana + " [" + str(self.hora_inicio) + " - " + str(self.hora_fin) + "]"

class Contacto(models.Model):
    idPublicidad = models.ForeignKey(Publicidad, on_delete = models.DO_NOTHING)
    telefono = models.CharField(max_length = 10)
    correo = models.CharField(max_length = 20)

class HiloChat(models.Model):
    #idHiloChat = models.AutoField(primary_key = True)
    idEmisora = models.ForeignKey(Emisora, on_delete=models.DO_NOTHING)
    dia = models.CharField(max_length = 9)

class MensajeChat(models.Model):
    #idMensaje = models.AutoField(primary_key = True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    idHiloChat = models.ForeignKey(HiloChat,  on_delete=models.CASCADE)
    mensaje = models.CharField(max_length = 500)

class Concursante(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 10)
    idUsuario = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.CharField(max_length = 1, default='A')

class Concurso(models.Model):
    idEncuesta = models.ForeignKey(Encuesta, on_delete=models.DO_NOTHING)
    premios = models.CharField(max_length = 500)
    ganador = models.ForeignKey(Concursante, on_delete=models.CASCADE)

class Pregunta(models.Model):
    contenido = models.CharField(max_length = 150)
    tipo = models.CharField(max_length = 1)
    respuesta_c = models.CharField(max_length = 150)
    idConcurso = models.ForeignKey(Concurso, on_delete=models.CASCADE)

class Respuesta(models.Model):
    idPregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    contenido = models.CharField(max_length = 150)
    correcta = models.CharField(max_length = 1)
    idConcursante = models.ForeignKey(Concursante, on_delete=models.CASCADE)

class Alternativa(models.Model):
    contenido = models.CharField(max_length = 150)
    idPregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)


class Telefono_Usuario(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    nro_telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.idUsuario.first_name + ' ' + self.idUsuario.last_name + ' : ' + self.nro_telefono

class RedSocial_usuario(models.Model):
    idUsuario= models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length = 20)
    link = models.CharField(max_length = 50)

class segmento_horario(models.Model):
    idSegmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    idHorario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idSegmento) + " : " + str(self.idHorario)

class segmento_usuario(models.Model):
    idSegmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class segmento_publicidad(models.Model):
    idSegmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    idPublicidad = models.ForeignKey(Publicidad, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.idSegmento) + " : " + str(self.idPublicidad)

class Telefono_emisora(models.Model):
    idEmisora = models.ForeignKey(Emisora, on_delete=models.CASCADE)
    nro_telefono = models.CharField(max_length=10)

    def __str__(self):
        return "{0} | {1}".format(self.idEmisora.nombre, self.nro_telefono)

class RedSocial_emisora(models.Model):
    idEmisora = models.ForeignKey(Emisora, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 25)
    link = models.CharField(max_length = 50)

    def __str__(self):
        return "{0} | {1}".format(self.idEmisora.nombre,self.nombre)

class frecuencia_publicidad(models.Model):
    idPublicidad = models.ForeignKey(Publicidad, on_delete = models.CASCADE)
    idFrecuencia = models.ForeignKey(Frecuencia, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.idPublicidad) + " : " + str(self.idFrecuencia)


class Auditoria(models.Model):
    accion = models.CharField(max_length = 50)
    tabla = models.CharField(max_length = 20)
    data_nueva = models.CharField(max_length = 50)
    data_actual = models.CharField(max_length = 50)
    fecha_creado = models.DateTimeField()
    fecha_modificado = models.DateTimeField(auto_now_add=True)

# Creación de Slugs
def create_slug(instance, sender, new_slug=None):
    slug = slugify(instance.nombre)
    if new_slug is not None:
        slug = new_slug
    qs = sender.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, sender, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Emisora)
@receiver(pre_save, sender=Segmento)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, sender)
