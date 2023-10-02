from rest_framework import serializers
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def create(self, validated_data):
        check_user = CustomUser.objects.filter(username=validated_data['username'])
        if check_user:
            return Response({'detail': 'This username is already in use'}, status=status.HTTP_401_UNAUTHORIZED)
        user = CustomUser.objects.create_user(validated_data)
        return user