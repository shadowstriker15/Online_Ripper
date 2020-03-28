import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import urllib.request
from pathlib import Path
import os


def get_album(album, user):
    client_id = "4b77fc0551f04b0b8778ba9edc045c23"
    client_secret = "f80bf5aabe724f7c89f2eb128639925d"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q='album:' + album, type='album')
    cover = str(results['albums']['items'][0]['images'][0]['url'])

    home = str(Path.home())
    path = os.path.join(home, 'Users', user, 'Downloads')

    urllib.request.urlretrieve(cover, os.path.join(path, "album.jpg"))
    return path
