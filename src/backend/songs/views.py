from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, check_json_body, assert_body_fields, assert_token

from .models import Song
from .serializers import SongSerializer

@check_method('GET')
def song_list(request: HttpRequest) -> JsonResponse:
    songs = Song.objects.all()
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()

@check_method('GET')
def song_detail(request: HttpRequest, song_pk: int) -> JsonResponse:
    song = Song.objects.get(pk=song_pk)
    serializer = SongSerializer(song, request=request)
    return serializer.json_response()

@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('song_id')
@assert_token
def like_song(request: HttpRequest) -> JsonResponse:
    song_id = request.data['song_id']
    song = Song.objects.get(id=song_id)
    if request.profile.liked_songs.filter(id=song_id).exists():
        request.profile.liked_songs.remove(song)
        return JsonResponse({'liked_songs': SongSerializer(request.profile.liked_songs.all()).serialize()})
    request.profile.liked_songs.add(song)
    return JsonResponse({'liked_songs': SongSerializer(request.profile.liked_songs.all()).serialize()})

@check_method('GET')
def latest_songs(request: HttpRequest) -> JsonResponse:
    songs = Song.objects.all().order_by('-added_at')[:5]
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()   

