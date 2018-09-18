from django.shortcuts import render
from rest_framework import generics

from WebAdminRadio import models
from . import serializers
# Create your views here.


class ListSegmento(generics.ListCreateAPIView):
    queryset = models.Segmento.objects.all()
    serializer_class = serializers.SegmentoSerializer