from django.contrib import admin

# Register your models here.
from .models import Album
admin.site.register(Album)

from .models import Photograph
admin.site.register(Photograph)