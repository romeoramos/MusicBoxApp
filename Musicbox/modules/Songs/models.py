from django.db import models
from modules.Artists.models import Artist
from django.conf import settings

# Create your models here.


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,related_name='artist_song')
    publication_date = models.DateField(null=True)
    cover = models.URLField(blank=True,null=True)
    rating = models.IntegerField(max_digits=1)
    category = models.CharField(max_length=100,choices=settings.CATEGORIES)
    song_file = FileField(uploadto="filename")
    user_creator =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE,related_name='song_comments')
    comment = models.TextField()
