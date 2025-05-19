from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared.utils import check_method, check_json_body, assert_body_fields, assert_token

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
@assert_body_fields('comment', 'score')
@assert_token
def add_review(request: HttpRequest, song_id: int) -> JsonResponse:
    song = Song.objects.get(id=song_id)
    new_review = Review.objects.create(
        author=request.profile,
        song=song,
        comment=request.data['comment'],
        score=request.data['score']
    )
    serializer = ReviewSerializer(new_review, request=request)
    return serializer.json_response()

@check_method('GET')
def latest_songs(request: HttpRequest) -> JsonResponse:
    songs = Song.objects.all().order_by('-added_at')[:5]
    serializer = SongSerializer(songs, request=request)
    return serializer.json_response()   

@check_method('GET')
def review_list(request: HttpRequest, song_id: int) -> JsonResponse:
    song = Song.objects.get(id=song_id)
    serializer = ReviewSerializer(song.reviews, request=request)
    return serializer.json_response()   

