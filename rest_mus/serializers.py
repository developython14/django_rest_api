from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = contact
        fields = ['created', 'title', 'icon_title', 'type_url' , 'url']


