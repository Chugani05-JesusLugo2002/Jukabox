from django.http import HttpRequest, JsonResponse

from shared.utils import check_method

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

@check_method('GET')
def latest_songs(request: HttpRequest) -> JsonResponse:
    songs = Song.objects.all().order_by('-added_at')[:5]
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()   

