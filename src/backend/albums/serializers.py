from shared.serializers import BaseSerializer

from artists.serializers import ArtistSerializer


class AlbumSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'mbid': instance.mbid,
            'title': instance.title,
            'artists': ArtistSerializer(instance.artists.all(), request=self.request).serialize(),
            'released_at': instance.released_at,
            'likes': instance.likes.count(),
            'cover': self.build_url(instance.cover.url),
            'added_at': instance.added_at.isoformat() 
        }
