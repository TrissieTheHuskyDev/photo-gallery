from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from gallery.serializers import AlbumSerializer,PhotographSerializer
from gallery.models import Album,Photograph


# API VIEWS FOR ALBUMS
class AlbumsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class AlbumList(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('title', 'description')
    pagination_class = AlbumsPagination

class AlbumCreate(CreateAPIView):
    serializer_class = AlbumSerializer

class AlbumRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    lookup_field = 'id'
    serializer_class = AlbumSerializer

    def delete(self, request, *args, **kwargs):
        album_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('album_data_{}'.format(album_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            album = response.data
            cache.set('album_data_{}'.format(album['id']), {
                'title': album['title'],
                'description': album['description'],
                'thumbnail': album['thumbnail'],
            })
        return response



# API VIEWS FOR PHOTOGRAPHS
class PhotographsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class PhotographList(ListAPIView):
    queryset = Photograph.objects.all()
    serializer_class = PhotographSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'description')
    pagination_class = AlbumsPagination

class PhotographCreate(CreateAPIView):
    serializer_class = PhotographSerializer

class PhotographRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Photograph.objects.all()
    lookup_field = 'id'
    serializer_class = PhotographSerializer

    def delete(self, request, *args, **kwargs):
        photograph_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('photograph_data_{}'.format(photograph_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            photograph = response.data
            cache.set('photograph_data_{}'.format(photograph['id']), {
                'album': photograph['album'],
                'name': photograph['name'],
                'description': photograph['description'],
                'photo': photograph['photo'],
                'creation_date': photograph['creation_date'],
            })
        return response
