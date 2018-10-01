from django import forms
from .models import Segmento

# Diccionario para definir el valor de 'name' en los inputs de los forms
FIELD_NAME_MAPPING = {
    'idEmisora': 'emisora'
}

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
        field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
        return super(SegmentoForm, self).add_prefix(field_name)
