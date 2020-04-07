from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    thumbnail = models.ImageField(upload_to='photos/', default = 'media/photos/no-image.png')
    
    def __str__(self):
        return self.title

class Photograph(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/', default = 'photos/no-image.png')
    description = models.TextField(max_length=1024)
    creation_date = models.DateField('date created')

    def __str__(self):
        return self.name