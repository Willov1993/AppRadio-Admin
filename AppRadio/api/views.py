from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
#Social media imports
#FACEBOOK
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
#TWITTER
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.social_serializers import TwitterLoginSerializer


from WebAdminRadio import models
from . import serializers
# Create your views here.


class ListSegmento(generics.ListCreateAPIView):
    queryset = models.Segmento.objects.all()
    serializer_class = serializers.SegmentoSerializer


class ListEmisora(generics.ListCreateAPIView):
    queryset = models.Emisora.objects.all()
    serializer_class = serializers.EmisoraSerializer




class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter



class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
