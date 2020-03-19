from django import forms
from .models import Link
from .download import youtube


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
        youtube(self, link)
        if not "youtube.com" in link:
            raise forms.ValidationError("This is not a valid YouTube link")
        return link
