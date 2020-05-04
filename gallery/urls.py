from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'gallery'
urlpatterns = [
    # '/gallery/
    path('', views.IndexView.as_view(), name='index'),
    # '/gallery/1/
    path('<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    # '/gallery/1/1/'
    path('<int:album_id>/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    # path('<int:album_id>/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    # '/gallery/about
    path('about', views.about, name='about'),

]