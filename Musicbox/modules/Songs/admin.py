from django.contrib import admin
from .models import Song,Comment

class SongAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Song, SongAdmin)
admin.site.register(Comment,CommentAdmin)
