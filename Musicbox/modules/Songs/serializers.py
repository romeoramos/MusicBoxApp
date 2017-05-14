from rest_framework import serializers
from .models import Song, Comment
from modules.Users.serializers import UserSerializer
from modules.Artists.serializers import ArtistSerializer
from modules.Albums.serializers import AlbumSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('user','comment')


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)
    user_creator = UserSerializer(read_only=True)
    song_comments = CommentSerializer(read_only=True,many=True)
    class Meta:
        model = Song
        #exclude = ("rating",)
        fields = ('id','name','artist','album','publication_date','cover','rating','category','song_file','user_creator','song_comments')
