from django.http import JsonResponse
import musicbrainzngs

from songs.models import Song
from artists.models import Artist
from albums.models import Album

class MusicBrainz:
    def __init__(self):
        musicbrainzngs.set_useragent('Jukabox', '1.0', 'jukabox.site@gmail.com')

    def create_artist(self, mbid: str) -> Artist:
        api_artist = musicbrainzngs.get_artist_by_id(mbid)['artist']
        artist = Artist.objects.create(
            mbid=mbid,
            name=api_artist['name']
        )
        return artist
    
    def create_song(self, mbid: str) -> JsonResponse:
        if Song.objects.filter(mbid=mbid).exists():
            return JsonResponse({'error': 'Song already exists'}, status=400)
        recording = musicbrainzngs.get_recording_by_id(mbid, includes=['artists', 'releases', 'tags'])['recording']
        artists = []
        for data in recording['artist-credit']:
            if isinstance(data, dict):
                artist_mbid = data['artist']['id']
                try:
                    artist = Artist.objects.get(mbid=artist_mbid)
                except Artist.DoesNotExist:
                    artist = self.create_artist(artist_mbid)
                finally:
                    artists.push(artist)
        release = recording['release-list'][0]
        release_year = int(release['date'][0:4])
          