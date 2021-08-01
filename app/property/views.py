from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from property.serializer import (
    InputPropertiesSerializer,
    OutputPropertiesSerializer,
)
from property import services as property_services
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework import serializers


class PropertiesView(APIView):
    """
    Get all properties avaliable on system, user can filter
    by year, city or state
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = InputPropertiesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        properties = property_services.search_properties(**data)
        output_serializer = OutputPropertiesSerializer(properties, many=True)
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)


class LikePropertiesView(APIView):
    """
    Like associated to autenticated user on received property
    """
    permission_classes = [IsAuthenticated]

    class InputPropertySerializer(serializers.Serializer):
        property_id = serializers.IntegerField(required=True)

    def post(self, request):
        serializer = self.InputPropertySerializer(data=request.data)
        current_user = request.user
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        property_services.like_properties(
            user_id=current_user.id,
            property_id=data.get('property_id')
        )
        return Response(data={}, status=status.HTTP_201_CREATED)


class UserAuth(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password")
        )
        if user is not None:
            # A backend authenticated the credentials

            try:
                token = Token.objects.get(user_id=user.id)

            except Token.DoesNotExist:
                token = Token.objects.create(user=user)

            return Response(token.key)

        else:
            # No backend authenticated the credentials
            return Response([], status=status.HTTP_401_UNAUTHORIZED)