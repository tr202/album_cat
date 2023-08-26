from albums.models import Album, AlbumSong, ArtistGroup, Song
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.register(
    (
        ArtistGroup,
        Song,
    )
)
admin.site.unregister(Group)


class AlbumSongInline(admin.TabularInline):
    model = AlbumSong


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "album_name",
        "artist_group",
        "release_year",
    )
    inlines = [
        AlbumSongInline,
    ]
