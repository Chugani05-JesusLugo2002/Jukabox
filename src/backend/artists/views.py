from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, assert_body_fields, check_json_body, assert_token

from .models import Artist
from .serializers import ArtistSerializer
from albums.serializers import AlbumSerializer

@check_method('GET')
def artist_list(request: HttpRequest) -> JsonResponse:
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, request=request)
    return serializer.json_response()

@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('artist_id')
@assert_token
def like_artist(request: HttpRequest) -> JsonResponse:
    artist_id = request.data['artist_id']
    artist = Artist.objects.get(id=artist_id)
    if request.profile.liked_artists.filter(id=artist_id).exists():
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
    serializer = AlbumSerializer(artist.albums.all(), request=request)
    return serializer.json_response()
    