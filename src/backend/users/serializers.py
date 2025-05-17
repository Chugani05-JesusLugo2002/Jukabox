from shared.serializers import BaseSerializer

from artists.serializers import ArtistSerializer
from albums.serializers import AlbumSerializer
from songs.serializers import SongSerializer


class UserSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'token': instance.token,
            'username': instance.user.username,
            'first_name': instance.user.first_name,
            'last_name': instance.user.last_name,
            'email': instance.user.email,
            'bio': instance.bio,
            'liked_songs': SongSerializer(instance.liked_songs.all(), request=self.request).serialize(),
            'liked_artists': ArtistSerializer(instance.liked_artists.all()).serialize(),
            'liked_albums': AlbumSerializer(instance.liked_albums.all(), request=self.request).serialize(),
            'avatar': self.build_url(instance.avatar.url)
        }
