from shared.serializers import BaseSerializer

from artists.serializers import ArtistSerializer
from albums.serializers import AlbumSerializer
from users.serializers import UserSerializer

from importer.serializers import LinkSerializer

class SongSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'mbid': instance.mbid,
            'title': instance.title,
            'artists': ArtistSerializer(instance.artists.all(), request=self.request).serialize(),
            'albums': AlbumSerializer(instance.albums.all(), request=self.request).serialize(),
            'cover': self.build_url(instance.cover),
            'added_at': instance.added_at.isoformat(),
            'likes': instance.likes.count(),
            'reviews': instance.reviews.count(),
            'lbz_url': instance.lbz_url,
        }
    

class ReviewSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'author': UserSerializer(instance.author, request=self.request).serialize(),
            'comment': instance.comment,
            'created_at': instance.created_at.isoformat(),
        }
