import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def find_albums(name):
    client_id = ""
    client_secret = ""
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']

    if len(items) != 0:
        artist = items[0]
        albums = []
        results = sp.artist_albums(artist['id'], album_type='album')
        albums.extend(results['items'])
        while results['next']:
            results = sp.next(results)
            albums.extend(results['items'])
        seen = set()  # to avoid dups
        albums.sort(key=lambda album: album['name'].lower())
        album_names = []
        for album in albums:
            album_link = album['external_urls']['spotify']
            name = album['name']

            if name not in seen:
                album_names.append((name, album_link))
                seen.add(name)

        return album_names

    else:
        return None
