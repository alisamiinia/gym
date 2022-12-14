from django.conf import UserSettingsHolder
from requests import request
from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer, UserGetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CreateUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions.IsAuthenticatedOrReadOnly


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        token = super().get_token(self.user)
        access_token = token.access_token
        access_token['role'] = User.objects.get(id=self.user.pk).role
        data['access'] = str(access_token)
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def get_user(request):
    try:
        #user = Customer.objects.get(pk=pk)
        userid = request.data['id']
        user = get_object_or_404(User, id = userid)
        user_ser = UserGetSerializer(user)
        user_ser.is_valid(raise_exception=True)
        #access_token = AccessToken(request)
        #user = User.objects.get(access_token['user_id'])
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
    #ser = UserGetSerializer(data = user)
    return Response(user_ser.data, status=status.HTTP_200_OK)







# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from knox.models import AuthToken
# from .serializers import UserSerializer, RegisterSerializer

# # Register API
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })

# from django.contrib.auth import login

# from rest_framework import permissions
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView

# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)