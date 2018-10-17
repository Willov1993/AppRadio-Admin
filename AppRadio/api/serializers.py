# api/serializers.py
from rest_framework import serializers
from WebAdminRadio import models


class SegmentoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'nombre',
            'slogan',
            'descripcion',
            'idEmisora',
            'imagen'
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