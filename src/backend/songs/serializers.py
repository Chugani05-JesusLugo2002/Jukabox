from shared.serializers import BaseSerializer

from artists.serializers import ArtistSerializer
from albums.serializers import AlbumSerializer


class GenreSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance):
        return {
            'id': instance.pk,
            'name': instance.name,
            'color': instance.color
        }
    

class SongSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        album = AlbumSerializer(instance.album, request=self.request).serialize() if instance.album else 'Single'

        return {
            'id': instance.pk,
            'title': instance.title,
            'artists': ArtistSerializer(instance.artists.all(), request=self.request).serialize(),
            'released_at': instance.released_at,
            'album': album,
            'cover': self.build_url(instance.cover),
            'genre': GenreSerializer(instance.genre.all()).serialize(),
            'added_at': instance.added_at.isoformat(),
        }
