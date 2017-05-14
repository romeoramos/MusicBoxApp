from django.conf.urls import url
from django.contrib import admin
from .views import ListSong, DetailSong

urlpatterns = [
    url(r'^$', ListSong.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DetailSong.as_view()),
]
