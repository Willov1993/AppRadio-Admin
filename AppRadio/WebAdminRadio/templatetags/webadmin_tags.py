from django import template
from ..models import Segmento, segmento_horario, Telefono_emisora, frecuencia_publicidad

register = template.Library()

# Devuelve los horarios de un segmento
@register.simple_tag
def get_horarios(segmento):
    return segmento_horario.objects.filter(idSegmento=segmento.id)

# Devuelve la cantidad de segmentos de una emisora
@register.simple_tag
def get_cant_segmentos(emisora):
    return Segmento.objects.filter(idEmisora=emisora, activo='A').count()

# Devuelve el teléfono de una emisora
@register.simple_tag
def get_telf_emisora(emisora):
    return Telefono_emisora.objects.get(idEmisora=emisora)

@register.simple_tag
def get_frecuencias(publicidad):
	return frecuencia_publicidad.objects.filter(idPublicidad=publicidad.id)


