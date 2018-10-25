# api/serializers.py
from rest_framework import serializers
from WebAdminRadio import models
from accounts.models import Usuario


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

class SegmentoSerializerToday(serializers.ModelSerializer):
    horarios = serializers.ReadOnlyField(source="get_horario_dia_actual")
    print(horarios)
    class Meta:
        model = models.Segmento
        fields = ('id', 'nombre', 'imagen', 'horarios')

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    def create(self, validated_data):

        usuario = Usuario.objects.create(
            username=validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            fecha_nac = validated_data['fecha_nac'],
            rol = validated_data['rol'],
        )
        usuario.set_password(validated_data['password'])
        usuario.save()

        return usuario

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
        model = Usuario
