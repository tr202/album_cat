from django.db import models


class ArtistGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    album_name = models.CharField(max_length=100, default=None, null=True, unique=True)
    artist_group = models.ForeignKey(ArtistGroup, on_delete=models.CASCADE)
    release_year = models.IntegerField()
    songs = models.ManyToManyField("Song", through="AlbumSong", related_name="albums")

    def __str__(self) -> str:
        return self.artist_group.name + " " + str(self.release_year)


class Song(models.Model):
    artist_group = models.ForeignKey(
        ArtistGroup, on_delete=models.CASCADE, related_name="songs"
    )
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name + "(" + self.artist_group.name + ")"


class AlbumSong(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="album_songs"
    )
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="song_albums")
    position = models.IntegerField()

    class Meta:
        constraints = (
            models.UniqueConstraint(
                name="no_double_position",
                fields=(
                    "album",
                    "position",
                ),
            ),
            models.UniqueConstraint(
                name="no_double_song",
                fields=(
                    "album",
                    "song",
                ),
            ),
        )
