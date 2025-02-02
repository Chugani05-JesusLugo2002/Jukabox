from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import json

from users.models import Profile
from users.serializers import UserSerializer

@csrf_exempt
def login(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    if (user := authenticate(request, username=username, password=password)):
        profile = Profile.objects.get(user=user)
        serializer = UserSerializer(profile, request=request)
        return serializer.json_response()
    

@csrf_exempt    
def signup(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    profile = Profile.objects.create(user=user)
    serializer = UserSerializer(profile, request=request)
    return serializer.json_response()

@csrf_exempt
def recover_user(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body)
    token = data['token']
    print(token)
    profile = Profile.objects.get(token=token)
    serializer = UserSerializer(profile, request=request)
    return serializer.json_response()