from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout

from shared.utils import check_method, assert_token, check_json_body, assert_body_fields
from songs.serializers import SongSerializer, ReviewSerializer
from artists.serializers import ArtistSerializer
from albums.serializers import AlbumSerializer

from .serializers import UserSerializer
from .models import Profile


@check_method('GET')
def user_list(request: HttpRequest) -> JsonResponse:
    users = Profile.objects.all()
    serializer = UserSerializer(users, request=request)
    return serializer.json_response()

@check_method('GET')
def user_detail(request: HttpRequest, user_slug: str) -> JsonResponse:
    try:
        user = Profile.objects.get(slug=user_slug)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'User not exists'}, status=404)
    serializer = UserSerializer(user, request=request)
    return serializer.json_response()

@check_method('GET')
@assert_token
def my_profile(request: HttpRequest) -> JsonResponse:
    serializer = UserSerializer(request.profile, request=request)
    return serializer.json_response()

@check_method('GET')
def liked_songs(request: HttpRequest, user_slug: str) -> JsonResponse:
    user = Profile.objects.get(slug=user_slug)
    serializer = SongSerializer(user.liked_songs.all(), request=request)
    return serializer.json_response()

@check_method('GET')
def liked_albums(request: HttpRequest, user_slug: str) -> JsonResponse:
    user = Profile.objects.get(slug=user_slug)
    serializer = AlbumSerializer(user.liked_albums.all(), request=request)
    return serializer.json_response()

@check_method('GET')
def liked_artists(request: HttpRequest, user_slug: str) -> JsonResponse:
    user = Profile.objects.get(slug=user_slug)
    serializer = ArtistSerializer(user.liked_artists.all(), request=request)
    return serializer.json_response()

@check_method('GET')
def user_reviews(request: HttpRequest, user_slug: str) -> JsonResponse:
    user = Profile.objects.get(slug=user_slug)
    serializer = ReviewSerializer(user.reviews.all(), request=request)
    return serializer.json_response()

@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('bio')
@assert_token
def change_profile(request: HttpRequest) -> JsonResponse:
    request.profile.bio = request.data['bio']
    request.profile.save()
    return JsonResponse({"message": "User profile changed!"})

@csrf_exempt
@check_method('POST')
@assert_token
def user_leave(request: HttpRequest) -> JsonResponse:
    logout(request)
    request.profile.user.delete()
    return JsonResponse({'message': 'See you later!'})