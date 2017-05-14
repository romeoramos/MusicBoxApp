from django.conf.urls import url
from django.contrib import admin
from .views import ListArtist, DetailArtist

urlpatterns = [
    url(r'^$', ListArtist.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DetailArtist.as_view()),
]
