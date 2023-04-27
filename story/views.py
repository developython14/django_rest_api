from django.contrib.auth.models import User, Group
from rest_framework import viewsets ,status
from rest_framework import permissions 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from .serializers import *
from django.http import Http404
from .models import *
from rest_framework import generics


from .serializers import *
from django.urls import path, include


class story_view(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = story.objects.all()
    serializer_class = storySerializer
    permission_classes = [permissions.AllowAny]



class story_image_view(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = story_image.objects.all()
    serializer_class = story_image_serializer
    permission_classes = [permissions.AllowAny]

    