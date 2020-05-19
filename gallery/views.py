from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.views import generic
# Create your views here.

from .models import Album,Photograph

# def index(request):
#     album_list = Album.objects.order_by('-title')
#     return render(request, 'gallery/index.html', {'album_list': album_list})
class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'album_list'

    def get_queryset(self):
        return Album.objects.order_by('title')

# def album_detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     photo_list = album.photograph_set.all()
#     return render(request, 'gallery/album_detail.html', 
#     {
#         'album': album,
#         'photo_list': photo_list,
#     })
class AlbumDetailView(generic.DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'gallery/album_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        self.album = get_object_or_404(Album, id=self.kwargs['pk'])
        context['photo_list'] = self.album.photograph_set.all()
        return context


class PhotoDetailView(generic.DetailView):
    model = Photograph
    context_object_name = 'start_photo'
    template_name = 'gallery/photo_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        self.album = get_object_or_404(Album, id=self.kwargs['album_id'])
        context['album'] = self.album
        context['photo_list'] = self.album.photograph_set.exclude(pk=self.kwargs['pk'])
        context['prev_photos'] = self.album.photograph_set.filter(pk__lt=self.kwargs['pk'])
        context['next_photos'] = self.album.photograph_set.filter(pk__gt=self.kwargs['pk'])
        return context

def about(request):
    return render(request, 'gallery/about.html')

def home(request):
    return render(request, 'gallery/home.html')
