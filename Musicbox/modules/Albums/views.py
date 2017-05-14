from django.shortcuts import render
from rest_framework import generics,filters,status
from .models import Album
from .serializers import AlbumSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.conf import settings
import django_filters.rest_framework

class ListAlbum(generics.ListCreateAPIView):

    #permission_classes = (IsAuthenticated,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('name','artist','category')
    search_fields = ('name','artist','category')


class DetailAlbum(generics.RetrieveUpdateDestroyAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
