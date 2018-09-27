from django import forms

class EmisoraForm(forms.Form):
    nombre= forms.CharField(max_length=150)
    frecuencia_dial = forms.RegexField(regex="[0-9]{2,3}\.[0-9] (AM|FM)",max_length=8)
    url_streaming = forms.URLField(max_length=150)
    sitio_web = forms.URLField(max_length=150, required=False)
    direccion = forms.CharField(max_length=250)
    descripcion = forms.CharField(max_length=500)
    ciudad = forms.RegexField(regex="[A-Za-z]+",max_length=50,strip=True)
    provincia = forms.RegexField(regex="[A-Za-z]+",max_length=50,strip=True)
    logotipo = forms.ImageField(required=False)

class TelefonoForm(forms.Form):
    telefono= forms.RegexField(regex="(\+)?[0-9]+",max_length = 10)

class RedSocialForm(forms.Form):
    nombre = forms.CharField(max_length = 25,required=False)
    link = forms.URLField(max_length = 50,required=False)

