from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, assert_token
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
def user_detail(request: HttpRequest, user_id: int) -> JsonResponse:
    user = Profile.objects.get(pk=user_id)
    serializer = UserSerializer(user, request=request)
    return serializer.json_response()

@check_method('GET')
@assert_token
def my_profile(request: HttpRequest) -> JsonResponse:
    serializer = UserSerializer(request.profile, request=request)
    return serializer.json_response()

@check_method('GET')
def liked_songs(request: HttpRequest, user_id: int) -> JsonResponse:
    user = Profile.objects.get(pk=user_id)
    serializer = SongSerializer(user.liked_songs.all(), request=request)
    return serializer.json_response()

@check_method('GET')
def liked_albums(request: HttpRequest, user_id: int) -> JsonResponse:
    user = Profile.objects.get(pk=user_id)
    serializer = AlbumSerializer(user.liked_albums.all(), request=request)
    return serializer.json_response()

@check_method('GET')
def liked_artists(request: HttpRequest, user_id: int) -> JsonResponse:
    user = Profile.objects.get(pk=user_id)
    serializer = ArtistSerializer(user.liked_artists.all(), request=request)
    return serializer.json_response()

@check_method('GET')
def user_reviews(request: HttpRequest, user_id: int) -> JsonResponse:
    user = Profile.objects.get(pk=user_id)
    serializer = ReviewSerializer(user.reviews.all(), request=request)
    return serializer.json_response()

@check_method('POST')
@assert_token
def change_profile(request: HttpRequest) -> JsonResponse:
    request.profile.bio = request.data['bio']
    request.profile.save()
    return JsonResponse({"message": "User profile changed!"})