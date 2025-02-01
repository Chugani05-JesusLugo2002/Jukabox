from django.http import HttpRequest, JsonResponse

from songs.serializers import SongSerializer

from .models import Playlist
from .serializers import PlaylistSerializer

def playlist_list(request: HttpRequest) -> JsonResponse:
    playlists = Playlist.objects.all()
    serializer = PlaylistSerializer(playlists, request=request)
    return serializer.json_response()

def playlist_songs(request: HttpRequest, playlist_pk: int) -> JsonResponse:
    playlist = Playlist.objects.get(pk=playlist_pk)
    songs = playlist.songs.all()
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()

def latest_playlist(request: HttpRequest) -> JsonResponse:
    playlists = Playlist.objects.all().order_by('-created_at')[:5]
    serializer = PlaylistSerializer(playlists, request=request)
    return serializer.json_response()
