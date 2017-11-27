# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from .models import User, UserSerializer


# Create your views here.
class UsersView(APIView):

    def get(self, request):
        users = UserSerializer(User.objects.all(), many=True)
        return Response(users.data)

    def put(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user.instance)
            token = jwt_encode_handler(payload)

            return Response({'token': token}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class UserView(APIView):

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data)

    def put(self, request, user_id):
        user = User.objects.get(pk=user_id)
        updated_user = UserSerializer(user, data=request.data)
        if updated_user.is_valid():
            updated_user.save()
            return Response(status=status.HTTP_202_ACCEPTED)

    def delete(self, request, user_id):
        count, aff = User.objects.get(pk=user_id).delete()
        if count is 1:
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def check_username(request):
    query = User.objects.filter(username__iexact=request.data['username'])

    if query.count() is 0:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def search_name(request, name):
    users = User.objects.filter(username__iexact=name)
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
