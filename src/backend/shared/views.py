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
    if not (query := request.data.get('query', '')):
        return JsonResponse({'error': 'Query not provided'}, status=400)
    match request.data['type']:
        case 'Artists':
            artists = Artist.objects.filter(name__icontains=query)
            artists_with_album = Artist.objects.filter(albums__title__icontains=query)
            queryset = artists | artists_with_album
            result = {'artists': ArtistSerializer(queryset.distinct(), request=request).serialize()}
        case 'Songs':
            songs = Song.objects.filter(title__icontains=query)
            songs_with_album = Song.objects.filter(albums__title__icontains=query)
            songs_with_artist = Song.objects.filter(artists__name__icontains=query)
            queryset = songs | songs_with_album | songs_with_artist
            result = {'songs': SongSerializer(queryset.distinct(), request=request).serialize()}
        case 'Albums':
            albums = Album.objects.filter(title__icontains=query)
            albums_with_song = Album.objects.filter(songs__title__icontains=query)
            albums_with_artist = Album.objects.filter(artists__name__icontains=query)
            queryset = albums | albums_with_song | albums_with_artist
            result = {'albums': AlbumSerializer(queryset.distinct(), request=request).serialize()}
        case _:
            result = {}
            artists = Artist.objects.filter(name__icontains=query)[:5]
            albums = Album.objects.filter(title__icontains=query)[:5]
            songs = Song.objects.filter(title__icontains=query)[:5]
            result['artists'] = ArtistSerializer(artists, request=request).serialize()
            result['albums'] = AlbumSerializer(albums, request=request).serialize()
            result['songs'] = SongSerializer(songs, request=request).serialize()

    return JsonResponse({'result': result})

