from rest_framework.generics import ListAPIView

from gallery.serializers import AlbumSerializer
from gallery.models import Album

class AlbumList(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer