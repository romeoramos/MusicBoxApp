from django.conf.urls import url
from django.contrib import admin
from .views import ListAlbum, DetailAlbum

urlpatterns = [
    url(r'^$', ListAlbum.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DetailAlbum.as_view()),
]
