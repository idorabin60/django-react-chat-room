from django.shortcuts import render
from rest_framework import viewsets
from .models import Server, Category, Chanel
from .serializer import ServerSerializer, CategorySerializer, ChanelSerializer
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse, Http404


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer  # Add the serializer class

    def list(self, request):
        category = request.query_params.get("category")

        qty = request.query_params.get("qty")
        id = request.query_params.get("server_id")
        with_num_members = request.query_params.get("num_members") == "true"
        if category:
            self.queryset = self.queryset.filter(category=category)
        if qty:
            self.queryset = self.queryset.filter(member__gt=qty)
        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))
        if id:
            try:
                by_server_id = int(id)
                print("asdasd")
                self.queryset = self.queryset.filter(id=id)
                if not self.queryset.exists():
                    raise ValidationError("server id does not exsists")

            except ValueError:
                raise Http404("invalid server id type is not int")

        serializer = ServerSerializer(
            self.queryset, many=True, context={"num_members": with_num_members}
        )
        return Response(serializer.data)
