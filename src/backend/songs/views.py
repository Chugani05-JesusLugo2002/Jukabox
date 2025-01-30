from .models import Song
from .serializers import SongSerializer

def song_list(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()
