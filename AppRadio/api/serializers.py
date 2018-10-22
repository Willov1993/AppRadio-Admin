# api/serializers.py
from rest_framework import serializers
from WebAdminRadio import models


class SegmentoSerializer(serializers.ModelSerializer):
    horarios = serializers.ReadOnlyField(source="get_horarios")
    class Meta:
        fields = (
            'id',
            'nombre',
            'slogan',
            'descripcion',
            'idEmisora',
            'imagen',
            'horarios'
        )
        model = models.Segmento

class EmisoraSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Emisora

class SegmentoSerializerFull(serializers.ModelSerializer):
    horarios = serializers.ReadOnlyField(source="get_horarios")
    print(horarios)

    class Meta:
        model = models.Segmento
        fields = ('id', 'nombre', 'imagen', 'horarios')
"""
class UsuarioSerializerNoVale(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'fecha_nac',
            'rol',
        )
        model = models.Usuario


class UserSerializer(serializers.Serializer):

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        )
        model = models.User

class UsuarioSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        fields = (
            'fecha_nac',
            'rol',
        )
        model = models.Usuario
"""
