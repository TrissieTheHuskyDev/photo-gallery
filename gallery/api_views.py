from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from gallery.serializers import AlbumSerializer
from gallery.models import Album

class AlbumList(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('title', 'description')