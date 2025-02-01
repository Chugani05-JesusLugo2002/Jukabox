from django.http import HttpRequest, JsonResponse

from .models import Album
from .serializers import AlbumSerializer

def album_list(request: HttpRequest) -> JsonResponse:
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, request=request)
    return serializer.json_response()

def album_detail(request: HttpRequest, album_pk: int) -> JsonResponse:
    album = Album.objects.get(pk=album_pk)
    serializer = AlbumSerializer(album, request=request)
    return serializer.json_response()

def latest_albums(request: HttpRequest) -> JsonResponse:
    albums = Album.objects.all().order_by('-added_at')[:5]
    serializer = AlbumSerializer(albums, request=request)
    return serializer.json_response()