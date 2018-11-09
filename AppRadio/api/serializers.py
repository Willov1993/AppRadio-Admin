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

#SEGMENTOS CON HORARIOS
class SegmentoSerializerFull(serializers.ModelSerializer):
    horarios = serializers.ReadOnlyField(source="get_horarios")

    class Meta:
        model = models.Segmento
        fields = ('id', 'nombre', 'imagen', 'idEmisora' , 'slogan', 'horarios')

#SEGMENTOS DEL DIA ACTUAL
class SegmentoSerializerToday(serializers.ModelSerializer):
    horarios = serializers.ReadOnlyField(source="get_horario_dia_actual")
    class Meta:
        model = models.Segmento
        fields = ('id', 'nombre', 'imagen', 'idEmisora' ,'horarios')

class LocutoresSerializer(serializers.ModelSerializer):
    emisora = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = (
            'id',
            'imagen',
            'first_name',
            'last_name',
            'emisora',
        )

    def get_emisora(self, obj):
        segmento_id = self.context.get('segmento')
        segmento_obj = models.segmento_usuario.objects.get(idSegmento=segmento_id, idUsuario=obj.id)
        return segmento_obj.idSegmento.idEmisora.nombre

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
            'id',
            'imagen',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'fecha_nac',
            'rol',
        )
        model = Usuario

class PublicidadSerializer(serializers.ModelSerializer):
    emisora = serializers.SerializerMethodField()
    frecuencia = serializers.ReadOnlyField(source = "get_frecuencia")

    class Meta:
        model = models.Publicidad
        fields = (
            'id',
            'imagen',
            'titulo',
            'cliente',
            'frecuencia',
            'emisora',
        )

    def get_emisora(self, obj):
        segmento_id = self.context.get('segmento')
        segmento_obj = models.segmento_publicidad.objects.get(idSegmento=segmento_id, idPublicidad=obj.id)
        return segmento_obj.idSegmento.idEmisora.nombre
