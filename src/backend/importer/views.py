from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, check_json_body, assert_body_fields

from .tasks import import_artist_data


@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('artist_mbid')
def import_artist(request: HttpRequest) -> JsonResponse:
    import_artist_data.delay(request.data['artist_mbid'])
    return JsonResponse({'message': f'Adding artist with MBID {request.data['artist_mbid']}'})