from django.http import HttpRequest, JsonResponse

from .models import Artist
from .serializers import ArtistSerializer

def artist_list(request: HttpRequest) -> JsonResponse:
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, request=request)
    return serializer.json_response()
    