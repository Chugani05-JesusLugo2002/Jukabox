from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from shared.utils import check_json_body, check_method, assert_body_fields

from users.models import Profile
from users.serializers import UserSerializer

@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('username', 'password')
def user_login(request: HttpRequest) -> JsonResponse:
    username = request.data['username']
    password = request.data['password']
    if (user := authenticate(request, username=username, password=password)):
        profile = Profile.objects.get(user=user)
        serializer = UserSerializer(profile, request=request)
        return serializer.json_response()
    return JsonResponse({'error': 'User not exists'}, status=404)


@csrf_exempt  
@check_method('POST')
@check_json_body
@assert_body_fields('username', 'password', 'first_name', 'last_name', 'email')  
def user_signup(request: HttpRequest) -> JsonResponse:
    username = request.data['username']
    if User.objects.filter(username=username).count() > 0:
        return JsonResponse({'error': 'Username already exists'}, status=409)
    email = request.data['email']
    if User.objects.filter(email=email).count() > 0:
        return JsonResponse({'error': 'Email already in use'}, status=409)
    user = User.objects.create_user(
        username=username,
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=email
    )
    profile = Profile.objects.create(user=user)
    serializer = UserSerializer(profile, request=request)
    return serializer.json_response()


@csrf_exempt
@check_method('GET')
def user_logout(request: HttpRequest) -> JsonResponse:
    logout(request)
    return JsonResponse({'message': 'User logged out'}, status=200)