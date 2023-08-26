from api.views import AlbumViewSet, ArtistGroupViewset, SongViewSet
from django.urls import include, path
from rest_framework import routers

app_name = "api"

router = routers.DefaultRouter()
router.register("artist_group", ArtistGroupViewset, basename="artist_group")
router.register("song", SongViewSet, basename="song")
router.register("album", AlbumViewSet, basename="album")


urlpatterns = [
    path("", include(router.urls)),
]
