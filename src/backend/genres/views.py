from django.http import HttpRequest, JsonResponse

from songs.serializers import SongSerializer

from .models import Genre
from .serializers import GenreSerializer

def genre_list(request: HttpRequest) -> JsonResponse:
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres)
    return serializer.json_response()

def genre_songs(request: HttpRequest, genre_slug: str) -> JsonResponse:
    genre = Genre.objects.get(slug=genre_slug)
    songs = genre.songs.all()
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()