from django.shortcuts import render
from rest_framework import viewsets
from .models import Server, Category, Chanel
from .serializer import ServerSerializer, CategorySerializer, ChanelSerializer
from rest_framework.response import Response


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer  # Add the serializer class

    def list(self, request):
        category = request.query_params.get("category")
        if category:
            query_set = self.queryset.filter(category=category)
        else:
            query_set = self.queryset
        serializer = ServerSerializer(query_set, many=True)
        return Response(serializer.data)
