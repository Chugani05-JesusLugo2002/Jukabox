from django.http import HttpRequest, JsonResponse

from .models import Artist
from .serializers import ArtistSerializer

def artist_list(request: HttpRequest) -> JsonResponse:
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, request=request)
    return serializer.json_response()

def artist_detail(request: HttpRequest, artist_pk: int) -> JsonResponse:
    artist = Artist.objects.get(pk=artist_pk)
    serializer = ArtistSerializer(artist, request=request)
    return serializer.json_response()

def latest_artists(request: HttpRequest) -> JsonResponse:
    artists = Artist.objects.all().order_by('-added_at')[:5]
    serializer = ArtistSerializer(artists, request=request)
    return serializer.json_response()
    