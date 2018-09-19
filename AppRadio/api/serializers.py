# api/serializers.py
from rest_framework import serializers
from WebAdminRadio import models


class SegmentoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'nombre',
            'slogan',
            'descripcion',
            'idEmsiora',
            'imagen',


        )
        model = models.Segmento

class EmisoraSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Emisora