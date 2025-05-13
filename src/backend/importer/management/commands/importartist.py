from django.core.management.base import BaseCommand, CommandError
import musicbrainzngs as mbz

from artists.models import Artist
from albums.models import Album
from songs.models import Song
from datetime import datetime

import os

class Command(BaseCommand):
    help = 'Delete all comments for the given post.'

    def add_arguments(self, parser):
        parser.add_argument('mbids', nargs='+', type=str)

    def handle(self, *args, **options):
        for mbid in options['mbids']:
            mbz.set_useragent('Jukabox', '0.1', 'jukabox.site@gmail.com')
            try:
                mbz_artist = mbz.get_artist_by_id(mbid, includes=['release-groups'])['artist']
            except:
                return 
            
            artist, created = Artist.objects.get_or_create(
                mbid=mbid,
                name=mbz_artist['name']
            )

            self.stdout.write(f'Getting information of artist {artist.name}...')

            for release_group in mbz_artist['release-group-list']:
                main_release = mbz.browse_releases(release_group=release_group['id'], release_status='official', limit=1, includes=['artist-credits'])['release-list']
                if main_release:
                    release_mbid = main_release[0]['id']
                    date = main_release[0]['date']
                    if date.count('-') == 2:
                        release_date = datetime.strptime(date, '%Y-%m-%d')
                    elif date.count('-') == 1:
                        release_date = datetime.strptime(date, '%Y-%m')
                    else:
                        release_date = datetime.strptime(date, '%Y')
                    album, created = Album.objects.get_or_create(
                        mbid=release_mbid,
                        title=main_release[0]['title'],
                        released_at=release_date
                    )

                    self.stdout.write(f'Saved information of album {album.title}.')

                    for release_artist in main_release[0]['artist-credit']:
                        artists = set()
                        artist, created = Artist.objects.get_or_create(
                            mbid=release_artist['artist']['id'],
                            name=release_artist['artist']['name']
                        )
                        artists.add(artist)
                    album.artists.set(artists)

                    try:
                        release_cover = mbz.get_image(release_mbid, 'front', '250')
                        if not release_cover is None:
                            release_cover_url = f'covers/cover-{release_mbid}.jpg'
                            file_path = os.path.join('media', release_cover_url)
                            with open(file_path, 'wb') as file:
                                file.write(release_cover)
                            album.cover = release_cover_url
                            album.save()
                    except mbz.ResponseError:
                        self.stdout.write(f'Error fetching cover for release {release_mbid}')


                    release_songs = mbz.browse_recordings(release=release_mbid)
                    for recording in release_songs['recording-list']:
                        song, created = Song.objects.get_or_create(
                            mbid=recording['id'],
                            title=recording['title']
                        )
                        if created:
                            self.stdout.write(f'Added song {song.title}')
                        song.albums.add(album)
                        song.save()
            
