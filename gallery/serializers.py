from rest_framework import serializers

from gallery.models import Album, Photograph

class PhotographSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        min_length=2, 
        max_length=50,
        style = {'placeholder': 'Enter name between 2-50 characters'}
    )
    description = serializers.CharField(
        min_length=5, 
        max_length=200,
        style = {'placeholder': 'Enter description between 5-200 characters'}
    )
    photo = serializers.ImageField(required=True)
    class Meta:
        model = Photograph
        fields = (
            'id','album', 'name', 'description', 'creation_date', 'photo'
        )

class AlbumSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        min_length=2, 
        max_length=50,
        style = {'placeholder': 'Enter name between 2-50 characters'}
    )
    description = serializers.CharField(
        min_length=5, 
        max_length=200,
        style = {'placeholder': 'Enter description between 5-200 characters'}
    )
    thumbnail = serializers.ImageField(default='photos/no-image.png')
    album_photos = serializers.SerializerMethodField()
    class Meta:
        model = Album
        fields = (
            'id', 'title', 'description', 'thumbnail', 'album_photos'
        )

    def get_album_photos(self, instance):
        photos = Photograph.objects.filter(album=instance)
        return PhotographSerializer(photos, many=True).data

    