from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
import musicbrainzngs as mbz

import requests
from PIL import Image
from io import BytesIO

from albums.models import Album
from artists.models import Artist
from songs.models import Song

class Command(BaseCommand):
    help = 'Add data from a MusicBrainz API release to the database'

    def add_arguments(self, parser):
        parser.add_argument('release_mbids', nargs='+', type=str)

    def handle(self, *args, **options):
        mbz.set_useragent('Jukabox', '0.1', 'jukabox.site@gmail.com')
        for mbid in options['release_mbids']:

            if Album.objects.filter(mbid=mbid).count() > 0:
                print("Album already exists in the database")
                break

            cover_url = 'http://coverartarchive.org/release/' + mbid
            image_url = f'covers/cover-{mbid}.jpg'
            response = requests.get(cover_url).json()

            if 'images' in response and len(response['images']) > 0:
                image_response = requests.get(response['images'][0]['thumbnails']['small'])
                
                if image_response.status_code == 200:
                    image = Image.open(BytesIO(image_response.content))
                    image.save(f'media/{image_url}')
                    print("Image successfully downloaded and saved: cover-{mbid}.jpg")
                else:
                    print("Failed to retrieve image")
            else:
                print("No images found in the response")
            

            release = mbz.get_release_by_id(mbid, includes=['recordings'])['release']
            release_date = datetime.strptime(release['date'], '%Y-%m-%d')

            album = Album.objects.create(mbid=mbid, title=release['title'], released_at=release_date.year, cover=image_url)
            
            release_artists = set()
            
            for medium in release['medium-list']:
                for track in medium['track-list']:
                    song_mbid = track['recording']['id']
                    song_data = mbz.get_recording_by_id(song_mbid, includes=['artists'])['recording']
                    song = Song(
                        mbid=song_mbid,
                        title=song_data['title']
                    )
                    print(f'Added {song.title}')
                    song_artists = set()
                    for artist_data in song_data['artist-credit']:
                        artist, created = Artist.objects.get_or_create(
                            mbid=artist_data['artist']['id'],
                            name=artist_data['artist']['name']
                        )
                        song_artists.add(artist)
                    release_artists.update(song_artists)
                    song.album = album
                    song.save()
                    song.artists.set(song_artists)
            album.artists.set(release_artists)



            