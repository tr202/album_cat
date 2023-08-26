from django_filters import rest_framework as filters
from albums.models import Song, AlbumSong
from django.db.models import OuterRef

class SongFilterSet(filters.FilterSet):
    album_id = filters.AllValuesMultipleFilter(field_name="albums__id")
    artist_group_id = filters.AllValuesMultipleFilter(field_name="artist_group__id")
    def filter_queryset(self, queryset):
        album_id = self.request.GET.get('album_id')
        queryset = super().filter_queryset(queryset)
        queryset = queryset.annotate(position=(AlbumSong.objects.filter(song=OuterRef('id'), album_id = album_id).values('position')))
        queryset = queryset.order_by('position')
        return queryset
    
    class Meta:
        model = Song
        fields = ("name",)
