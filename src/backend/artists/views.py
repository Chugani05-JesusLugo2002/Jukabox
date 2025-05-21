from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, assert_token
from albums.serializers import AlbumSerializer
from songs.serializers import SongSerializer
from importer.serializers import LinkSerializer

from .models import Artist
from .serializers import ArtistSerializer

@check_method('GET')
def artist_list(request: HttpRequest) -> JsonResponse:
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, request=request)
    return serializer.json_response()

@csrf_exempt
@check_method('POST')
@assert_token
def like_artist(request: HttpRequest, artist_pk: int) -> JsonResponse:
    artist = Artist.objects.get(pk=artist_pk)
    if request.profile.liked_artists.filter(pk=artist_pk).exists():
        request.profile.liked_artists.remove(artist)
        return JsonResponse({'liked_artists': ArtistSerializer(request.profile.liked_artists.all()).serialize()})
    request.profile.liked_artists.add(artist)
    return JsonResponse({'liked_artists': ArtistSerializer(request.profile.liked_artists.all()).serialize()})

@check_method('GET')
def artist_detail(request: HttpRequest, artist_pk: int) -> JsonResponse:
    artist = Artist.objects.get(pk=artist_pk)
    serializer = ArtistSerializer(artist, request=request)
    return serializer.json_response()

@check_method('GET')
def artist_albums(request: HttpRequest, artist_pk: int) -> JsonResponse:
    artist = Artist.objects.get(pk=artist_pk)
    serializer = AlbumSerializer(artist.albums.all().order_by('title'), request=request)
    return serializer.json_response()

@check_method('GET')
def artist_top_albums(request: HttpRequest, artist_pk: int) -> JsonResponse:
    artist = Artist.objects.get(pk=artist_pk)
    queryset = artist.albums.all().order_by('-likes')[:6]
    serializer = AlbumSerializer(queryset, request=request)
    return serializer.json_response()

@check_method('GET')
def artist_songs(request: HttpRequest, artist_pk: int) -> JsonResponse:
    artist = Artist.objects.get(pk=artist_pk)
    serializer = SongSerializer(artist.songs.all().order_by('albums__title'), request=request)
    return serializer.json_response()

@check_method('GET')
def artist_top_songs(request: HttpRequest, artist_pk: int) -> JsonResponse:
    artist = Artist.objects.get(pk=artist_pk)
    queryset = artist.songs.all().order_by('-likes')[:6]
    serializer = SongSerializer(queryset, request=request)
    return serializer.json_response()

@check_method('GET')
def artist_links(request: HttpRequest, artist_pk: int) -> JsonResponse:
    artist = Artist.objects.get(pk=artist_pk)
    serializer = LinkSerializer(artist.links.all())
    return serializer.json_response()