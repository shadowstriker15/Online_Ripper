import glob
from pathlib import Path
import os

home = str(Path.home())
user_path = os.path.join(home, 'Users')

users_path = []
p = Path(user_path)

for user in p.iterdir():
    user = os.path.join(user, 'Downloads')
    users_path.append(user)

user_songs = []
user_covers = []

for path in users_path:
    songs = os.path.join(path, '*mp3')
    covers = os.path.join(path, '*jpg')

    songs = glob.glob(songs)
    covers = glob.glob(covers)
    user_songs.append(songs)
    user_covers.append(covers)

for user in user_songs:
    for cover in user:
        os.remove(cover)

for user in user_covers:
    for song in user:
        os.remove(song)