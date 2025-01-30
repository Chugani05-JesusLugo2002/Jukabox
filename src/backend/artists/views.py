from django.http import HttpRequest, JsonResponse

from .serializers import ArtistSerializer
from .models import Artist

def artist_list(request: HttpRequest) -> JsonResponse:
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, request=request)
    return serializer.json_response()
    