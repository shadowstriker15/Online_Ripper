from django import forms
from django.core.exceptions import ValidationError

from .models import Song


class RawLinkForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(RawLinkForm, self).__init__(*args, **kwargs)
        self.fields['link'].label = ""

    link = forms.URLField(max_length=500,
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder": "Enter YouTube link here ex: https://www.youtube.com/a-song-or-playlist-link",
                                  'size': 80,
                              }
                          )
                          )

    def clean_link(self):
        link = self.cleaned_data.get("link")
        if "youtube.com" not in link:
            raise ValidationError("Enter a valid YouTube link")
        return link


class RawSongForm(forms.Form):
    artist = forms.CharField(max_length=100,
                             widget=forms.TextInput()
                             )
    album = forms.CharField(max_length=100,
                            widget=forms.TextInput()
                            )
    title = forms.CharField(max_length=100,
                            widget=forms.TextInput()
                            )
    genre = forms.ChoiceField(choices=Song.genreList)


class FindAlbumsForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(FindAlbumsForm, self).__init__(*args, **kwargs)
        self.fields['find_artist'].label = ""

    find_artist = forms.CharField(max_length=100,
                                  widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "Artist name here",
                                      }
                                  )
                                  )
