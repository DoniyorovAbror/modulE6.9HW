from rest_framework.serializers import ModelSerializer
from .models import *



class RoomSerializer(ModelSerializer):
    class Meta:
        model = chatroom
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'