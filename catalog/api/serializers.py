from albums.models import Album, AlbumSong, ArtistGroup, Song
from rest_framework import serializers


class ArtistGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistGroup
        fields = ("name",)


class AlbumSongSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="song.name")

    class Meta:
        model = AlbumSong
        fields = (
            "name",
            "position",
        )


class ShortAlbumSerialiser(serializers.ModelSerializer):
    artist_group = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Album
        fields = ("album_name", "artist_group", "release_year")


class AlbumSerializer(ShortAlbumSerialiser):
    songs = AlbumSongSerializer(source="album_songs", many=True)

    class Meta:
        model = Album
        fields = ("album_name", "artist_group", "release_year", "songs")


class SongSerializer(serializers.ModelSerializer):
    artist_group = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Song
        fields = (
            "artist_group",
            "name",
        )


class SongAlbumSerializer(SongSerializer):
    position = serializers.IntegerField()

    class Meta:
        model = Song
        fields = (
            "name",
            "position",
        )
