from django.db import models
from django.conf import settings
from django.conf import settings

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    bio = models.TextField()
    category = models.CharField(max_length=100,choices=settings.CATEGORIES)
    user_creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
