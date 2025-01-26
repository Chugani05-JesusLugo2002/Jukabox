# Django Plan

## Models

### Song

1. title: CharField
2. artist: M2M -> Artist
3. released_at: DateField
4. album: FK -> Album (optional)
5. genre: M2M -> Genre
6. url: URLField

### Artist

1. name: CharField
2. uuid: UUIDField
3. bio: TextField

### Album

1. title: CharField
2. artist: M2M -> Artist