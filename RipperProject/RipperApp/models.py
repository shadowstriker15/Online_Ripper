from django.core.validators import FileExtensionValidator
from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=200)


class Song(models.Model):
    genreList = (("No genre", " "),
                 ("Alternative", "Alternative"),
                 ("Blues/R&B", "Blues/R&B"),
                 ("Books & Spoken", "Books & Spoken"),
                 ("Children's Music", "Children's Music"),
                 ("Classic Rock", "Classic Rock"),
                 ("Classic Rock/Rock", "Classic Rock/Rock"),
                 ("Classical", "Classical"),
                 ("Country", "Country"),
                 ("Dance", "Dance"),
                 ("Easy Listening", "Easy Listening"),
                 ("Electronic", "Electronic"),
                 ("Folk", "Folk"),
                 ("Hip Hop/Rap", "Hip Hop/Rap"),
                 ("Holiday", "Holiday"),
                 ("House", "House"),
                 ("Industrial", "Industrial"),
                 ("Jazz", "Jazz"),
                 ("Leftfield", "Leftfield"),
                 ("New Age", "New Age"),
                 ("Other", "Other"),
                 ("Pop", "Pop"),
                 ("Pop/Rock", "Pop/Rock"),
                 ("R&B", "R&B"),
                 ("R&B/Soul", "R&B/Soul"),
                 ("Religious", "Religious"),
                 ("Rock", "Rock"),
                 ("Rock & Roll", "Rock & Roll"),
                 ("Soundtrack", "Soundtrack"),
                 ("Techno", "Techno"),
                 ("Trance", "Trance"),
                 ("Unclassifiable", "Unclassifiable"),
                 ("Vocal", "Vocal"),
                 ("World", "World"))

    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=genreList, default=" ")

