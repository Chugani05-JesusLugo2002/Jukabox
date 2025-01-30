from django.http import HttpRequest, JsonResponse

from .models import Song, Genre
from .serializers import SongSerializer

def song_list(request: HttpRequest) -> JsonResponse:
    songs = Song.objects.all()
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()

def song_detail(request: HttpRequest, song_pk: int) -> JsonResponse:
    song = Song.objects.get(pk=song_pk)
    serializer = SongSerializer(song, request=request)
    return serializer.json_response()

def latest_songs(request: HttpRequest) -> JsonResponse:
    songs = Song.objects.all().order_by('added_at')[:5]
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()