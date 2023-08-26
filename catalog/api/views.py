from albums.models import Album, ArtistGroup, Song
from api.filters import SongFilterSet
from api.serializers import (
    AlbumSerializer,
    ArtistGroupSerializer,
    ShortAlbumSerialiser,
    SongAlbumSerializer,
    SongSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ArtistGroupViewset(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    queryset = ArtistGroup.objects.all()
    serializer_class = ArtistGroupSerializer


class AlbumViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Album.objects.all().select_related("artist_group")
    serializer_class = AlbumSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ShortAlbumSerialiser
        return super().list(request, *args, **kwargs)


class SongViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Song.objects.select_related("artist_group")
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SongFilterSet

    def get_serializer_class(self):
        if self.request.GET.get("album_id"):
            return SongAlbumSerializer
        return SongSerializer
