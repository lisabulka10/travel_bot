from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.db import transaction

from .models import User
from profiles.models import UserProfile


class TokenPairSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('tg_id', 'password', 'username',)

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        profile = UserProfile.objects.create(user=user)
        return user
