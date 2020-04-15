from django.urls import path

from . import views, api_views

app_name = 'gallery'
urlpatterns = [
    path('api/v1/albums', api_views.AlbumList.as_view()),

    # '/gallery/
    path('', views.index, name='index'),
    # '/gallery/1/
    path('<int:album_id>/', views.album_detail, name='album_detail'),
    # '/gallery/1/1/'
    path('<int:album_id>/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    # '/gallery/about
    path('about', views.about, name='about'),

]