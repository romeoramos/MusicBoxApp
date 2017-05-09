from django.db import models
from modules.Songs.models import Song
from modules.Artists.models import Artist
from django.conf import settings

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,related_name='artist_album')
    songs = models.ManyToManyField(Song, blank=True) #Aquí no se si es ManyToManyField
    category = category = models.CharField(max_length=100,choices=settings.CATEGORIES)
