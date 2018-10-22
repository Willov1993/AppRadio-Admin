from django import forms
from .models import Segmento, Horario, Publicidad, Frecuencia

# field_name_mapping es el diccionario con los names que estarán en los forms,
# que no deben ser iguales a los campos de los modelos

class EmisoraForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    frecuencia_dial = forms.RegexField(regex=r"[0-9]{2,3}\.[0-9] (AM|FM)", max_length=8)
    url_streaming = forms.URLField(max_length=150)
    sitio_web = forms.URLField(max_length=150, required=False)
    direccion = forms.CharField(max_length=250)
    descripcion = forms.CharField(max_length=500)
    ciudad = forms.RegexField(regex="[A-Za-z]+", max_length=50, strip=True)
    provincia = forms.RegexField(regex="[A-Za-z]+", max_length=50, strip=True)
    logotipo = forms.ImageField(required=False)

class TelefonoForm(forms.Form):
    telefono = forms.RegexField(regex=r"(\+)?[0-9]+", max_length=10)

class RedSocialForm(forms.Form):
    nombre = forms.CharField(max_length=25, required=False)
    link = forms.URLField(max_length=50, required=False)

class PublicidadForm(forms.ModelForm):
    class Meta:
        model = Publicidad
        fields = [
            'titulo',
            'cliente',
            'descripcion',
            'url',
            'imagen'
            ]

class FrecuenciaForm(forms.ModelForm):
    class Meta:
        model = Frecuencia
        fields = [
            'tipo',
            'dia_semana',
            'hora_inicio',
            'hora_fin'
            ]

    def add_prefix(self, field_name):
        field_name_mapping = {
            'fecha_inicio': 'inicio',
            'fecha_fin': 'fin'
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(HorarioForm, self).add_prefix(field_name)


class SegmentoForm(forms.ModelForm):
    class Meta:
        model = Segmento
        fields = [
            'nombre',
            'slogan',
            'descripcion',
            'idEmisora',
            'imagen'
        ]


    # Esta función define el atributo 'name' con el valor del diccionario
    def add_prefix(self, field_name):
        field_name_mapping = {
            'idEmisora': 'emisora'
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(SegmentoForm, self).add_prefix(field_name)

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'dia',
            'fecha_inicio',
            'fecha_fin'
        ]

    def add_prefix(self, field_name):
        field_name_mapping = {
            'fecha_inicio': 'inicio',
            'fecha_fin': 'fin'
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(HorarioForm, self).add_prefix(field_name)
