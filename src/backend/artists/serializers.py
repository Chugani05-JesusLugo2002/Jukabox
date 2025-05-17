from shared.serializers import BaseSerializer


class ArtistSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance):
        return {
            'id': instance.pk,
            'mbid': instance.mbid,
            'name': instance.name,
            'bio': instance.bio,
            'added_at': instance.added_at.isoformat(),
            'likes': instance.likes.count()
        }