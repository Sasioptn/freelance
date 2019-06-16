from rest_framework import generics

from . import models
from . import serializers
from rest_framework import viewsets
class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset =  models.CustomUser.objects.all()
    serializer_class = serializers.UserRegisterSerializer
