# serializers.py
from rest_framework import serializers
from .models import Category, Server, Chanel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"


class ChanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chanel
        fields = "__all__"
