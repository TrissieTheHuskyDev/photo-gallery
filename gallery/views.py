from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Album,Photograph

def index(request):
    album_list = Album.objects.order_by('-title')[:5]
    context = {'album_list': album_list}
    return render(request, 'gallery/index.html', context)

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'gallery/album_detail.html', {'album': album})

def photo_detail(request, album_id, photo_id):
    photo = get_object_or_404(Photograph, pk = photo_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'gallery/photo_detail.html', {'photo': photo, 'album':album})
