from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return "user_image/%s/%s" %(instance.id, filename)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nac = models.DateField()
    imagen = models.ImageField(upload_to = upload_location, blank=True)
    rol = models.CharField(max_length = 1)

class Emisora(models.Model):
    #idEmisora = models.AutoField(primary_key = True)
    nomnbre = models.CharField(max_length = 150)
    frecuencia_dial = models.CharField(max_length = 8)
    url_streaming = models.CharField(max_length = 150)
    sitio_web = models.CharField(max_length = 150)
    direccion = models.CharField(max_length = 250)
    descripcion = models.CharField(max_length = 500)
    ciudad = models.CharField(max_length = 50)
    provincia = models.CharField(max_length = 50)

class Segmento(models.Model):
    #idSegmento = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 150)
    slogan = models.CharField(max_length = 150)
    descripcion = models.CharField(max_length = 250)
    idEmsiora = models.ForeignKey(Emisora, on_delete=models.DO_NOTHING)
    imagen = models.CharField(max_length = 250)

class Encuesta(models.Model):
    #idEncuesta = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 150)
    descripcion = models.CharField(max_length = 250)
    imagen = models.CharField(max_length = 250)
    fecha_inicio = models.DateTimeField(auto_now_add=True)

class Horario(models.Model):
    #idHorario = models.AutoField(primary_key = True)
    fecha_inicio = models.DateTimeField()
    fehca_fin = models.DateTimeField()

class Publicidad(models.Model):
    titulo = models.CharField(max_length = 150)
    cliente = models.CharField(max_length = 80)
    descripcion = models.CharField(max_length = 350)
    url = models.CharField(max_length = 150)
    estado = models.CharField(max_length = 1)
    imagen = models.ImageField(upload_to = upload_location, blank=None)

class Tipo_sugerencia(models.Model):
    nombre = models.CharField(max_length = 15)
    descripcion = models.CharField(max_length = 500)

class Sugerencia(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    mensaje = models.CharField(max_length = 250)
    idUsuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)
    idEmisora = models.ForeignKey(Emisora, on_delete = models.DO_NOTHING)
    idTipo = models.ForeignKey(Tipo_sugerencia, on_delete = models.DO_NOTHING)

class Frecuencia(models.Model):
    duracion = models.DateTimeField()
    tipo = models.CharField(max_length = 1)
    dia_semana = models.CharField(max_length = 9, blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null = True)
    nro_dias = models.IntegerField()

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

class RedSocial_usuario(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length = 20)
    link = models.CharField(max_length = 50)

class segmento_horario(models.Model):
    idSegmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    idHorario = models.ForeignKey(Horario, on_delete=models.CASCADE)

class segmento_usuario(models.Model):
    idSegmento = models.ForeignKey(Segmento, on_delete = models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

class segmento_publicidad(models.Model):
    idSegmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    idPublicidad = models.ForeignKey(Publicidad, on_delete = models.CASCADE)

class Telefono_emisora(models.Model):
    idEmisora = models.ForeignKey(Emisora, on_delete=models.CASCADE)
    nro_telefono = models.CharField(max_length = 10)

class RedSocial_emisora(models.Model):
    idEmisora = models.ForeignKey(Emisora, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 25)
    link = models.CharField(max_length = 50)

class frecuencia_publicidad(models.Model):
    idSegmento = models.ForeignKey(Segmento, on_delete = models.CASCADE)
    idFrecuencia = models.ForeignKey(Frecuencia, on_delete = models.CASCADE)

class Auditoria(models.Model):
    accion = models.CharField(max_length = 50)
    tabla = models.CharField(max_length = 20)
    data_nueva = models.CharField(max_length = 50)
    data_actual = models.CharField(max_length = 50)
    fecha_creado = models.DateTimeField()
    fecha_modificado = models.DateTimeField(auto_now_add=True)