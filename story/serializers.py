from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class story_image_serializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = story_image
        fields = [ 'id', 'image',
                ]


class storySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = story
        fields = ['id','created', 'page_de_garde', 'order' , 'snippets']


