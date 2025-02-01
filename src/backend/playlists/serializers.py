from shared.serializers import BaseSerializer

from songs.serializers import SongSerializer
from users.serializers import UserSerializer

class PlaylistSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'title': instance.title,
            'songs': SongSerializer(instance.songs.all(), request=self.request).serialize(),
            'user': UserSerializer(instance.user).serialize(),
            'created_at': instance.created_at.isoformat()
        }
