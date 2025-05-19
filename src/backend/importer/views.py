from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, check_json_body, assert_body_fields

from .tasks import import_artist_data

import musicbrainzngs as mbz    


@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('artist_mbid')
def import_artist(request: HttpRequest) -> JsonResponse:
    mbid = request.data['artist_mbid']
    import_artist_data.delay(mbid)
    return JsonResponse({'message': f'Adding artist with MBID {mbid}'})

@csrf_exempt
def test(request):
    mbz.set_useragent('Jukabox', '0.1', 'jukabox.site@gmail.com')
    artist = mbz.get_artist_by_id('a6c6897a-7415-4f8d-b5a5-3a5e05f3be67', includes=['url-rels'])
    return JsonResponse({'result': artist})