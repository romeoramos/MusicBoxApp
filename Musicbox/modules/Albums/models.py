from django.db import models
from modules.Artists.models import Artist
from django.conf import settings

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,related_name='artist_album')
    category = models.CharField(max_length=100,choices=settings.CATEGORIES)
    user_creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
