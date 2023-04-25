from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class story_image_serializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='story.id')

    class Meta:
        model = story_image
        fields = [ 'id', 'image', 'owner',
                 ]


class storySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    storiess = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model = story
        fields = ['id','created', 'page_de_garde', 'storiess']


