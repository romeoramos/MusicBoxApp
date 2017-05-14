from rest_framework import serializers
from .models import Album
from modules.Users.serializers import UserSerializer
from modules.Artists.serializers import ArtistSerializer

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("__all__")
