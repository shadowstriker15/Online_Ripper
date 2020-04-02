import os

import eyed3


def editor(artist, title, album, genre, path_list, album_path):
    audio_file = eyed3.load(path_list[0])
    audio_file.tag.artist = artist
    audio_file.tag.title = title
    audio_file.tag.album = album
    audio_file.tag.genre = genre

    # filename = os.path.basename(picture_path)

    audio_file.tag.images.set(3, open(album_path, 'rb').read(), 'image/jpeg')
    os.remove(album_path)

    audio_file.tag.save()

    path_list = path_list[1:]
