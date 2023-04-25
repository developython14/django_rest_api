from django.contrib.auth.models import User, Group
from rest_framework import viewsets ,status
from rest_framework import permissions 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from .serializers import *
from django.http import Http404
from .models import *


from .serializers import *
from django.urls import path, include


    




class crebview(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]



def toma(request):
    print('request come fine')
    print(request.data)
    print(request.body)
    return  HttpResponse("Hello, world. You're at the polls index.")