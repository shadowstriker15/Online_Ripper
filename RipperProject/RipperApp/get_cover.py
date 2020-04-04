import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import urllib.request
from pathlib import Path
import os


# Used to find and download an album cover

def find_cover(album, user):
    client_id = ""
    client_secret = ""
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q='album:' + album, type='album')

    # Checking if valid album
    if len(results['albums']['items']) == 0:
        return None
    else:
        cover = str(results['albums']['items'][0]['images'][0]['url'])

        home = str(Path.home())
        path = os.path.join(home, 'Users', user, 'Downloads', "album.jpg")

        urllib.request.urlretrieve(cover, path)
        return path
