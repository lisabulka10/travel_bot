from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import (
    RegisterSerializer,
    TokenPairSerializer,
)


@extend_schema_view(
    post=extend_schema(
        summary="Получение JWT токенов",
        description="Аутентификация по tg_id и паролю. Возвращает access и refresh токены.",
        tags=["authenticate"]
    )
)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


@extend_schema_view(
    post=extend_schema(
        summary="Обновление access токена",
        description="Обновление access токена по refresh токену.",
        tags=["authenticate"]
    )
)
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(
    summary="Регистрация нового пользователя",
    request=RegisterSerializer,
    responses={
        201: OpenApiResponse(description="Пользователь успешно создан"),
        400: OpenApiResponse(description="Ошибка валидации"),
    },
    tags=["authenticate"]
)
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.to_representation(user), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

