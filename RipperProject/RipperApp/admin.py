from django.contrib import admin

from .models import Link, Song, Document

admin.site.register(Link)
admin.site.register(Song)
admin.site.register(Document)