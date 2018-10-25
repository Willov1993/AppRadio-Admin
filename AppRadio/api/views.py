from rest_framework import generics
#Social media imports
#FACEBOOK
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
#TWITTER
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.social_serializers import TwitterLoginSerializer


from WebAdminRadio import models
from accounts.models import Usuario
from . import serializers
from rest_framework import mixins
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

import datetime
# Create your views here.

DIAS=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

class ListSegmento(generics.ListCreateAPIView):
    queryset = models.Segmento.objects.all()
    serializer_class = serializers.SegmentoSerializer

class ListSegmentosDiaActual(generics.ListAPIView):
    day= datetime.datetime.today().weekday()
    dia_actual=DIAS[day]
    horariosDelDia= models.Horario.objects.filter(dia=dia_actual)
    ids_segmentos= models.segmento_horario.objects.filter(idHorario__in=horariosDelDia).distinct()
    queryset=  models.Segmento.objects.filter(pk__in=ids_segmentos.values('idSegmento'))
    serializer_class= serializers.SegmentoSerializerToday

class ListSegmentosEmisoraDiaActual(generics.ListAPIView):
    serializer_class= serializers.SegmentoSerializerToday

    def get_queryset(self):
        emisora = self.kwargs['id_emisora']
        day= datetime.datetime.today().weekday()
        dia_actual=DIAS[day]
        horariosDelDia= models.Horario.objects.filter(dia=dia_actual)
        ids_segmentos= models.segmento_horario.objects.filter(idHorario__in=horariosDelDia).distinct()
        return models.Segmento.objects.filter(pk__in=ids_segmentos.values('idSegmento'),idEmisora=emisora)


class ListEmisora(generics.ListCreateAPIView):
    queryset = models.Emisora.objects.all()
    serializer_class = serializers.EmisoraSerializer

class CreateUser(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class CreateUserA(APIView,mixins.CreateModelMixin):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

class ListEmisoraSegmento(generics.ListAPIView):
    serializer_class = serializers.SegmentoSerializerFull

    def get_queryset(self):
        emisora = self.kwargs['id_emisora']
        return models.Segmento.objects.filter(idEmisora=emisora)
