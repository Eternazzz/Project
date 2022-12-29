from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import *
from django.contrib.auth import authenticate


class UserSignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSignInView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSignInSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSignInSerializer(data=request.data)
        serializer.is_valid()
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            raise ValidationError({"400": f'Аккаунта с таким e-mail не существует'})
        user = authenticate(username=email, password=password, request=request)
        if user is not None:
            return Response({'user': user.email}, status=status.HTTP_200_OK)
        else:
            raise ValidationError({"400": f'Неверный пароль'})
