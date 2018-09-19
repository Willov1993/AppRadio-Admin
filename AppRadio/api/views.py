from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt

from WebAdminRadio import models
from . import serializers
# Create your views here.


class ListSegmento(generics.ListCreateAPIView):
    queryset = models.Segmento.objects.all()
    serializer_class = serializers.SegmentoSerializer


class ListEmisora(generics.ListCreateAPIView):
    queryset = models.Emisora.objects.all()
    serializer_class = serializers.EmisoraSerializer