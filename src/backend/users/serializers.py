from shared.serializers import BaseSerializer


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
            'avatar': self.build_url(instance.avatar.url),
            'slug': instance.slug,
            'liked_songs_count': instance.liked_songs.count(),
            'liked_albums_count': instance.liked_albums.count(),
            'liked_artists_count': instance.liked_artists.count(),
            'reviews_count': instance.reviews.count()
        }
