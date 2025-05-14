from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from albums.models import Album
from albums.serializers import AlbumSerializer
from artists.models import Artist
from artists.serializers import ArtistSerializer
from songs.models import Song
from songs.serializers import SongSerializer
from .utils import check_method, check_json_body, assert_body_fields


@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('query', 'type')
def explore(request: HttpRequest) -> JsonResponse:
    query = request.data['query']
    match request.data['type']:
        case 'Artists':
            artists = Artist.objects.filter(name__icontains=query)[:9]
            result = {'artists': ArtistSerializer(artists, request=request).serialize()}
        case 'Songs':
            songs = Song.objects.filter(title__icontains=query)[:9]
            result = {'songs': SongSerializer(songs, request=request).serialize()}
        case 'Albums':
            albums = Album.objects.filter(title__icontains=query)[:9]
            result = {'albums': AlbumSerializer(albums, request=request).serialize()}
        case _:
            result = {}
            artists = Artist.objects.filter(name__icontains=query)[:3]
            albums = Album.objects.filter(title__icontains=query)[:3]
            songs = Song.objects.filter(title__icontains=query)[:3]
            result['artists'] = ArtistSerializer(artists, request=request).serialize()
            result['albums'] = AlbumSerializer(albums, request=request).serialize()
            result['songs'] = SongSerializer(songs, request=request).serialize()

    return JsonResponse({'result': result})

