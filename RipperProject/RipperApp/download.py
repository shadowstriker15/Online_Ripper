import youtube_dl
from pathlib import Path
import os


def yt_download(link, account):
    home = str(Path.home())
    user = str(account)

    archive_path = os.path.join(home, 'Users', user, 'Downloads', 'archive.txt')
    out_path = os.path.join(home, 'Users', user, 'Downloads', '%(title)s.%(ext)s')

    # Download data and config
    download_options = {
        'format': 'bestaudio/best',
        'outtmpl': out_path,
        'nocheckcertificate': True,
        'download_archive': archive_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(download_options) as dl:
        dl.download([link])
