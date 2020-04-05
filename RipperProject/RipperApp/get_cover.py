import urllib.request
from pathlib import Path
import os


# Used to find and download an album cover

def find_cover(link, user):
    home = str(Path.home())
    path = os.path.join(home, 'Users', user, 'Downloads', "album.jpg")

    urllib.request.urlretrieve(link, path)
    return path
