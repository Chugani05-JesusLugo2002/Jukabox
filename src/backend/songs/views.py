from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, check_json_body, assert_body_fields, assert_token
from importer.serializers import LinkSerializer

from .models import Song, Review
from .serializers import SongSerializer, ReviewSerializer

@check_method('GET')
def song_list(request: HttpRequest) -> JsonResponse:
    songs = Song.objects.all()
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()

@check_method('GET')
def song_detail(request: HttpRequest, song_pk: int) -> JsonResponse:
    song = Song.objects.get(pk=song_pk)
    serializer = SongSerializer(song, request=request)
    return serializer.json_response()


@check_method('GET')
def song_links(request: HttpRequest, song_pk: int) -> JsonResponse:
    song = Song.objects.get(pk=song_pk)
    result = [LinkSerializer(album.links.all()).serialize() for album in song.albums.all()]
    return JsonResponse(result[0], safe=False)


@csrf_exempt
@check_method('POST')
@assert_token
def like_song(request: HttpRequest, song_pk: int) -> JsonResponse:
    song = Song.objects.get(pk=song_pk)
    if request.profile.liked_songs.filter(pk=song_pk).exists():
        request.profile.liked_songs.remove(song)
    else:
        request.profile.liked_songs.add(song)
    return JsonResponse({'liked_songs': SongSerializer(request.profile.liked_songs.all()).serialize()})

@csrf_exempt
@check_method('POST')
@check_json_body
@assert_body_fields('comment')
@assert_token
def add_review(request: HttpRequest, song_pk: int) -> JsonResponse:
    song = Song.objects.get(pk=song_pk)
    new_review = Review.objects.create(
        author=request.profile,
        song=song,
        comment=request.data['comment'],
    )
    serializer = ReviewSerializer(new_review, request=request)
    return serializer.json_response()

@check_method('GET')
def latest_songs(request: HttpRequest) -> JsonResponse:
    songs = Song.objects.all().order_by('-added_at')[:5]
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()   

@check_method('GET')
def song_reviews(request: HttpRequest, song_pk: int) -> JsonResponse:
    song = Song.objects.get(pk=song_pk)
    serializer = ReviewSerializer(song.reviews.all().order_by('-created_at'), request=request)
    return serializer.json_response()   

