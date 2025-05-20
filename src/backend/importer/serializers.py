from shared.serializers import BaseSerializer

class LinkSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'url': instance.url,
            'url_type': instance.url_type 
        }
