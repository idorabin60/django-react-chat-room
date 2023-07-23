# serializers.py
from rest_framework import serializers
from .models import Category, Server, Chanel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ChanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chanel
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):
    num_members = serializers.SerializerMethodField()
    chanel_server = ChanelSerializer(many=True)

    class Meta:
        model = Server
        exclude = ("member",)

    def get_num_members(self, obj):
        if hasattr(obj, "num_members"):
            return obj.num_members
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not self.context.get("num_members"):
            data.pop("num_members", None)
        return data
