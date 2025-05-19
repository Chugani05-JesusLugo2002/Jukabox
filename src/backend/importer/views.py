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