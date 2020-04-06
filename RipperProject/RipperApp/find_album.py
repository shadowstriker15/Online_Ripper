from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


def get_album(name, title):
    client_id = ""
    client_secret = ""
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']

    # Check if artist is in Spotify's database
    if len(items) == 0:
        return "Invalid", "Invalid"

    artist = items[0]
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    seen = set()  # to avoid dups
    albums.sort(key=lambda album: album['name'].lower())
    for album in albums:
        name = album['name']
        if name not in seen:
            seen.add(name)

    album_dict = {}
    cover_dict = {}

    for album in albums:
        track_list = []
        name = album['name']
        cover = album['images'][0]['url']
        tracks = []
        results = sp.album_tracks(album['id'])
        tracks.extend(results['items'])
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        for track in tracks:
            track_list.append(track['name'])
        album_dict.update({name: track_list})
        cover_dict.update({name: cover})

    for album in album_dict:
        if title in album_dict[album]:
            cover_album = album
            cover_link = cover_dict[cover_album]
            return cover_album, cover_link

    # Track not in album or artist only has singles
    album = title + " " + name
    results = sp.search(q='album:' + album, type='album')

    # Can't find album cover
    if len(results['albums']['items']) == 0:
        return "Invalid", "Invalid"

    cover = str(results['albums']['items'][0]['images'][0]['url'])
    return album, cover
