from django import forms
from django.core.exceptions import ValidationError

from .models import Link, Song


class RawLinkForm(forms.Form):
    link = forms.URLField(max_length=500,
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder": "ex: https://www.youtube.com/watch?v=q6EoRBvdVPQ&list=PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo",
                              }
                          )
                          )

    def clean_link(self):
        link = self.cleaned_data.get("link")
        if not "youtube.com" in link:
            raise ValidationError("This is not a valid YouTube link")
        return link


class RawSongForm(forms.Form):

    artist = forms.CharField(max_length=100,
                             widget=forms.TextInput()
                             )
    title = forms.CharField(max_length=100,
                            widget=forms.TextInput()
                            )
    album = forms.CharField(max_length=100,
                            widget=forms.TextInput()
                            )
    genre = forms.ChoiceField(choices=Song.genreList)
