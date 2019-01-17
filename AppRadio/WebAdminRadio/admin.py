from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Usuario)
admin.site.register(Emisora)
admin.site.register(Segmento)
admin.site.register(Encuesta)
admin.site.register(Horario)
admin.site.register(Publicidad)
admin.site.register(Tipo_sugerencia)
admin.site.register(Sugerencia)
admin.site.register(Frecuencia)
admin.site.register(Contacto)
admin.site.register(HiloChat)
admin.site.register(MensajeChat)
admin.site.register(Concursante)
admin.site.register(Concurso)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Alternativa)
admin.site.register(Telefono_emisora)
admin.site.register(RedSocial_emisora)
admin.site.register(Telefono_Usuario)
admin.site.register(RedSocial_usuario)
admin.site.register(segmento_horario)
admin.site.register(segmento_usuario)
admin.site.register(segmento_publicidad)
admin.site.register(frecuencia_publicidad)
admin.site.register(Auditoria)
admin.site.register(Imagenes)
admin.site.register(Videos)