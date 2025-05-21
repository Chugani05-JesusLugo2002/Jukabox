from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, check_json_body, assert_body_fields, assert_token
from songs.serializers import SongSerializer
from importer.serializers import LinkSerializer

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

@csrf_exempt
@check_method('POST')
@assert_token
def like_album(request: HttpRequest, album_pk: int) -> JsonResponse:
    album = Album.objects.get(pk=album_pk)
    if request.profile.liked_albums.filter(pk=album_pk).exists():
        request.profile.liked_albums.remove(album)
        return JsonResponse({'message': f'Un-like to {album.title}!'})
    request.profile.liked_albums.add(album)
    return JsonResponse({'message': f'Like to {album.title}!'})

@check_method('GET')
def latest_albums(request: HttpRequest) -> JsonResponse:
    albums = Album.objects.all().order_by('-added_at')[:6]
    serializer = AlbumSerializer(albums, request=request)
    return serializer.json_response()

@check_method('GET')
def most_liked_albums(request: HttpRequest) -> JsonResponse:
    albums = Album.objects.all().order_by('-likes')[:6]
    serializer = AlbumSerializer(albums, request=request)
    return serializer.json_response()

@check_method('GET')
def album_links(request: HttpRequest, album_pk: int) -> JsonResponse:
    album = Album.objects.get(pk=album_pk)
    serializer = LinkSerializer(album.links.all())
    return serializer.json_response()