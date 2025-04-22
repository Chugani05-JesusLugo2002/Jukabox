from django.http import HttpRequest, JsonResponse

from shared.utils import check_method
from songs.serializers import SongSerializer

from .models import Album
from .serializers import AlbumSerializer

@check_method('GET')
def album_list(request: HttpRequest) -> JsonResponse:
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, request=request)
    return serializer.json_response()

@check_method('GET')
def album_detail(request: HttpRequest, album_pk: int) -> JsonResponse:
    album = Album.objects.get(pk=album_pk)
    serializer = AlbumSerializer(album, request=request)
    return serializer.json_response()


@check_method('GET')
def album_songs(request: HttpRequest, album_pk: int) -> JsonResponse:
    album = Album.objects.get(pk=album_pk)
    songs = album.songs.all()
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()

@check_method('GET')
def latest_albums(request: HttpRequest) -> JsonResponse:
    albums = Album.objects.all().order_by('-added_at')[:5]
    serializer = AlbumSerializer(albums, request=request)
    return serializer.json_response()