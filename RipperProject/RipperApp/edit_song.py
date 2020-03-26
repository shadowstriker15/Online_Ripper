import os

import eyed3


def editor(artist, title, album, path_list, picture_path=None):
    audio_file = eyed3.load(path_list[0])
    audio_file.tag.artist = artist
    audio_file.tag.title = title
    audio_file.tag.album = album

    picture_path = 'C:\\Users\\austi\\Downloads\\Album Covers\\Currents Album Cover.jpg'

    # filename = os.path.basename(picture_path)

    audio_file.tag.images.set(3, open(picture_path, 'rb').read(), 'image/jpeg')

    audio_file.tag.save()

    path_list = path_list[1:]
