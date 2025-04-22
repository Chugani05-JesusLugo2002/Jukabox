from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from shared.utils import check_json_body, check_method

from users.models import Profile
from users.serializers import UserSerializer

@csrf_exempt
@check_method('POST')
@check_json_body
def login(request: HttpRequest) -> JsonResponse:
    username = request.data['username']
    password = request.data['password']
    if (user := authenticate(request, username=username, password=password)):
        profile = Profile.objects.get(user=user)
        serializer = UserSerializer(profile, request=request)
        return serializer.json_response()
    

@csrf_exempt  
@check_method('POST')
@check_json_body  
def signup(request: HttpRequest) -> JsonResponse:
    username = request.data['username']
    password = request.data['password']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['email']

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
@check_method('POST')
@check_json_body
def recover_user(request: HttpRequest) -> JsonResponse:
    token = request.data['token']
    profile = Profile.objects.get(token=token)
    serializer = UserSerializer(profile, request=request)
    return serializer.json_response()
