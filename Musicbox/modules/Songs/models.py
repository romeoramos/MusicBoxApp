from django.db import models
from modules.Artists.models import Artist
from modules.Albums.models import Album
from django.conf import settings

# Create your models here.

def song_directory_path(intance,filename):
    return 'songs/{0}'.format(filename)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,related_name='artist_song')
    album = models.ForeignKey(Album,on_delete=models.CASCADE,related_name='album_song')
    publication_date = models.DateField(null=True)
    cover = models.URLField(blank=True,null=True)
    rating = models.IntegerField()
    category = models.CharField(max_length=100,choices=settings.CATEGORIES)
    song_file = models.FileField(upload_to=song_directory_path)
    user_creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE,related_name='song_comments')
    user_comment = models.TextField()
