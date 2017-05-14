from django.shortcuts import render
from rest_framework import generics,filters,status
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
#from rest_framework.parsers import FormParser,MultiPartParser
#from rest_framework.response import Response
from django.conf import settings
import django_filters.rest_framework
# Create your views here.

class ListArtist(generics.ListCreateAPIView):

    #permission_classes = (IsAuthenticated,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('name','nationality','category')
    search_fields = ('name','nationality','category')


class DetailArtist(generics.RetrieveUpdateDestroyAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
