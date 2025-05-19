import django_rq

import musicbrainzngs as mbz
import os
import logging
from datetime import datetime

from artists.models import Artist
from albums.models import Album
from songs.models import Song
from .models import ArtistLink, AlbumLink, SongLink

logger = logging.getLogger(__name__)

def import_cover_data(release_mbid: str, album: Album):
    try:
        release_cover = mbz.get_image(release_mbid, 'front', '250')
        logger.info(release_cover)
        if release_cover is None:
            logger.info('No cover data found!')
        else:
            release_cover_url = f'covers/cover-{release_mbid}.jpg'
            file_path = os.path.join('media', release_cover_url)
            try:
                with open(file_path, 'wb') as file:
                    file.write(release_cover)
                album.cover = release_cover_url
                album.save()
            except Exception as e:
                logger.info(f'Error saving cover image: {e}')
    except mbz.ResponseError as e:
        logger.info(f'Error fetching cover data: {e}')

@django_rq.job
def import_artist_data(mbid: str):
    mbz.set_useragent('Jukabox', '0.1', 'jukabox.site@gmail.com')
    try:
        mbz_artist = mbz.get_artist_by_id(mbid, includes=['release-groups', 'url-rels'])['artist']
    except:
        return 
    
    artist, created = Artist.objects.get_or_create(
        mbid=mbid,
        name=mbz_artist['name']
    )

    for url in mbz_artist['url-relation-list']:
        if url['type'] == 'free streaming':
            artist_link = ArtistLink.objects.get_or_create(
                url=url['target'],
                artist=artist
            )

    for release_group in mbz_artist['release-group-list']:
        main_release = mbz.browse_releases(release_group=release_group['id'], release_status='official', limit=1, includes=['artist-credits', 'url-rels'])['release-list']
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

            for url in main_release[0]['url-relation-list']:
                if url['type'] == 'free streaming':
                    album_link = AlbumLink.objects.get_or_create(
                        url=url['target'],
                        album=album
                    )

            for release_artist in main_release[0]['artist-credit']:
                artists = set()
                artist, created = Artist.objects.get_or_create(
                    mbid=release_artist['artist']['id'],
                    name=release_artist['artist']['name']
                )
                artists.add(artist)
            album.artists.set(artists)

            queue = django_rq.get_queue('default')
            download_cover_job = queue.enqueue(import_cover_data, release_mbid, album)

            release_songs = mbz.browse_recordings(release=release_mbid, includes=['url-rels'])
            logger.info(release_songs)
            for recording in release_songs['recording-list']:
                song, created = Song.objects.get_or_create(
                    mbid=recording['id'],
                    title=recording['title']
                )
                song.albums.add(album)
                song.artists.set(album.artists.all())
                song.save()

                for url in recording['url-relation-list']:
                    if url['type'] == 'free streaming':
                        song_link = SongLink.objects.get_or_create(
                            url=url['target'],
                            song=song
                        )