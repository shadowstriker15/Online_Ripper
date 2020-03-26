from django.core.validators import FileExtensionValidator
from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=200)


class Song(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    # genre = models.Choices(value=0)


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
