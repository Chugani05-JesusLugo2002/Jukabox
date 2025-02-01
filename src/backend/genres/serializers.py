from shared.serializers import BaseSerializer


class GenreSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance):
        return {
            'id': instance.pk,
            'name': instance.name,
            'slug': instance.slug,
            'color': instance.color
        }