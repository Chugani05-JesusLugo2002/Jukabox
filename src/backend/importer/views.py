from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, check_json_body, assert_body_fields

from .tasks import import_artist_data

import musicbrainzngs as mbz

from artists.models import Artist

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
        main_release = mbz.browse_releases(release_group=release_group['id'], release_status='official', limit=1)['release-list']
        if main_release:
            release_songs = mbz.browse_recordings(release=main_release[0]['id'])
        
    
    return JsonResponse({'result': result})