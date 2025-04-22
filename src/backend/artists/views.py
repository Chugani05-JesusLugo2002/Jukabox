from django.http import HttpRequest, JsonResponse

from shared.utils import check_method

from .models import Artist
from .serializers import ArtistSerializer


@check_method('GET')
def artist_list(request: HttpRequest) -> JsonResponse:
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, request=request)
    return serializer.json_response()


@check_method('GET')
def artist_detail(request: HttpRequest, artist_pk: int) -> JsonResponse:
    artist = Artist.objects.get(pk=artist_pk)
    serializer = ArtistSerializer(artist, request=request)
    return serializer.json_response()


@check_method('GET')
def latest_artists(request: HttpRequest) -> JsonResponse:
    artists = Artist.objects.all().order_by('-added_at')[:5]
    serializer = ArtistSerializer(artists, request=request)
    return serializer.json_response()
    