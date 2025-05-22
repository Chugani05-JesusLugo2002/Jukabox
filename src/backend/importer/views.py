from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import re

from shared.utils import check_method, check_json_body, assert_body_fields, assert_token

from .tasks import import_artist_data


@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('artist_mbid')
@assert_token
def import_artist(request: HttpRequest) -> JsonResponse:
    mbid = request.data['artist_mbid']
    mbid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    if not (m := re.fullmatch(mbid_pattern, mbid)):
        return JsonResponse({'error': 'Invalid MBID'}, status=400)
    import_artist_data.delay(mbid)
    return JsonResponse({'message': f'Updating artist data...'})
