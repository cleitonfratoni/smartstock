from django.shortcuts import render

# Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Models
from accounts.models import User as UserModel

# Serializers
from accounts.serializers import UserSerializer

@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':
        users = UserModel.objects.all()

        serializerd_user = UserSerializer(users, many=True)
        return Response(serializerd_user.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_user(request):

    if request.method == 'POST':
        serializer_user = UserSerializer(data=request.data)
        if serializer_user.is_valid():
            serializer_user.save()
            return Response(serializer_user.data, status=status.HTTP_201_CREATED)
    return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)
