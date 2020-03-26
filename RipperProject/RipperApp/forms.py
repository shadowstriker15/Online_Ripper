from django import forms

from .models import Link


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
            raise forms.ValidationError("This is not a valid YouTube link")
        return link


class RawSongForm(forms.Form):
    genres = ["Alternative", "Blues/R&B", "Books & Spoken", "Children's Music", "Classic Rock",
              "Classic Rock/Rock", "Classical", "Country", "Dance", "Easy Listening", "Electronic", "Folk",
              "Hip Hop/Rap", "Holiday", "House", "Industrial", "Jazz", "Leftfield", "New Age", "Other", "Pop",
              "Pop/Rock", "R&B", "R&B/Soul", "Religious", "Rock", "Rock & Roll", "Soundtrack", "Techno", "Trance",
              "Unclassifiable", "Vocal", "World"]

    artist = forms.CharField(max_length=100,
                             widget=forms.TextInput()
                             )
    title = forms.CharField(max_length=100,
                            widget=forms.TextInput()
                            )
    album = forms.CharField(max_length=100,
                            widget=forms.TextInput()
                            )
    # genre


class DocumentForm(forms.Form):
    # docfile = forms.FileField(label='Select archive.txt file')
    docfile = forms.FileField(widget=forms.FileInput(attrs={'accept':'.jpg'}),
                              label='Select .jpeg file')
