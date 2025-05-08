from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, check_json_body, assert_body_fields

from .tasks import import_artist_data

import musicbrainzngs as mbz
from datetime import datetime

from artists.models import Artist
from albums.models import Album
from songs.models import Song

@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('artist_mbid')
def import_artist(request: HttpRequest) -> JsonResponse:
    # Aqui empieza el codigo del job (hay que pasarlo a tasks.py)
    mbz.set_useragent('Jukabox', '0.1', 'jukabox.site@gmail.com')
    artist_mbid = request.data['artist_mbid']
    try:
        mbz_artist = mbz.get_artist_by_id(artist_mbid, includes=['release-groups'])['artist']
    except:
        return JsonResponse({'error': 'Invalid MBID'}, status=400)
    
    artist, created = Artist.objects.get_or_create(
        mbid=artist_mbid,
        name=mbz_artist['name']
    )

    for release_group in mbz_artist['release-group-list']:
        main_release = mbz.browse_releases(release_group=release_group['id'], release_status='official', limit=1, includes=['artist-credits'])['release-list']
        if main_release:
            release_mbid = main_release[0]['id']
            release_date = datetime.strptime(main_release[0]['date'], '%Y-%m-%d')
            album, created = Album.objects.get_or_create(
                mbid=release_mbid,
                title=main_release[0]['title'],
                released_at=release_date
            )

            for release_artist in main_release[0]['artist-credit']:
                artists = set()
                artist, created = Artist.objects.get_or_create(
                    mbid=release_artist['artist']['id'],
                    name=release_artist['artist']['name']
                )
                artists.add(artist)
            album.artists.set(artists)

            if created:
                release_cover = mbz.get_image(release_mbid, 'front', '500')
                release_cover_url = f'covers/cover-{release_mbid}.jpg'
                with open(f'media/{release_cover_url}', 'wb') as file:
                    file.write(release_cover)
                    album.cover = release_cover_url
                    album.save()

            release_songs = mbz.browse_recordings(release=release_mbid)
            for recording in release_songs['recording-list']:
                song, created = Song.objects.get_or_create(
                    mbid=recording['id'],
                    title=recording['title'],
                    album=album
                )
            
        
    
    return JsonResponse({'result': result})