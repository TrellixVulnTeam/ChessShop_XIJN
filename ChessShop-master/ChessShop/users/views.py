from django.shortcuts import redirect, render 
from . import models
from .forms import CreateUserForm
from main import urls
from rest_framework.decorators import api_view
from rest_framework.Response import Response
from rest_framework.auththoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializer import RegisterSerializer

# Create your views here.
@api_view(["POST"])
def login_api(request):
    _serializer = AuthTokenSerializer(data=request.data)
    _serializer.is_valid(raise_exception=True)
    user = _serializer.validated_data['users']
    _,token = AuthToken.objects.create(user)
    return Response({
        "user info":{
            'id': user.id,
             'firstName': user.firstName,
             'lastName': user.lastName,
             'patronymic': user.patronymic,
             'profilePicture': user.profilePicture,
             'gender': user.gender,
             'city': user.city,
             'experience':user.experience
        },
        "token":token
    })

@api_view(["GET"])
def get_user_data(request):
    user = request.user
    if user.is_authenticated():
        return Response({
            "user_info":{
                'id': user.id,
             'firstName': user.firstName,
             'lastName': user.lastName,
             'patronymic': user.patronymic,
             'profilePicture': user.profilePicture,
             'gender': user.gender,
             'city': user.city,
             'experience':user.experience
            }
        })

@api_view(["POST"])
def register_api(request):
    serializer = RegisterSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    user = serializer.save()
    _,token = AuthToken.objects.create(user=user)
    return Response({
        "user info":{
            'id': user.id,
             'firstName': user.firstName,
             'lastName': user.lastName,
             'patronymic': user.patronymic,
             'profilePicture': user.profilePicture,
             'gender': user.gender,
             'city': user.city,
             'experience':user.experience
        },
        "token":token
    })