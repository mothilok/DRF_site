from rest_framework import serializers
from .models import Poster

class Serializer_post(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'

class Serializer_create_post(serializers.ModelSerializer):
    class Meta:
        model = Poster
        exclude = ('miniature', 'author')