from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


@api_view(['GET', 'POST'])
def user_list_view(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            queryset = User.objects.filter(pk=pk).first()
            serializer = UserSerializer(queryset)
            return Response(serializer.data)
    elif request.method == 'PUT':
        queryset = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        queryset = User.objects.filter(pk=pk).first().delete()
        return Response("Eliminado!")
    
