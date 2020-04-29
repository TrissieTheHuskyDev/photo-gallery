# from django.test import TestCase
from rest_framework.test import APITestCase

from gallery.models import Album

# Create your tests here.

class AlbumCreateTestCase(APITestCase):
    def test_create_album(self):
        initial_album_count = Album.objects.count()
        album_attrs = {
            'title': 'New Album',
            'description': 'This is a new album',
        }
        response = self.client.post('/api/v1/albums/new', album_attrs)
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(
            Album.objects.count(),
            initial_album_count + 1,
        )
        for attr, expected_value in album_attrs.items():
            self.assertEqual(response.data[attr], expected_value)

class AlbumListAPIView(APITestCase):
    def test_list_albums(self):
        albums_count = Album.objects.count()
        response = self.client.get('/api/v1/albums')
        print("Album Count: ",albums_count)
        print("Response Count: ",response.data['count'])
        self.assertEqual(response.data['count'], albums_count)
        self.assertEqual(len(response.data['results']), albums_count)

        