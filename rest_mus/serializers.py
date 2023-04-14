from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = contact
        fields = ['id','created', 'title', 'icon_title', 'type_url' , 'url']


