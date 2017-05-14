from django.shortcuts import render
from rest_framework import generics,filters,status
from .models import Song
from .serializers import SongSerializer
import django_filters.rest_framework
#from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
#from rest_framework.parsers import FormParser,MultiPartParser
#from rest_framework.response import Response
from django.conf import settings
# Create your views here.

class ListSong(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('name','artist','album','category')
    search_fields = ('name','artist','album','category')


class DetailSong(generics.RetrieveUpdateDestroyAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer
