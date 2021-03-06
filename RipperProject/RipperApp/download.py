import youtube_dl
from pathlib import Path
import os
from urllib.parse import urlsplit


# Used to download and convert YouTube videos

def yt_download(link, account):
    home = str(Path.home())
    user = str(account)
    out_path = os.path.join(home, 'Users', user, 'Downloads', '%(title)s.%(ext)s')

    cookie_file = os.path.join(home, 'Cookies', 'cookies.txt')

    # Create archive if a playlist link
    if "playlist" in link:
        parse_result = urlsplit(link)
        query = parse_result.query
        archive_path = os.path.join(home, 'Users', user, 'Downloads', 'Archives', query)
        if not os.path.exists(archive_path):
            os.makedirs(archive_path)

        archive_file = os.path.join(home, 'Users', user, 'Downloads', 'Archives', query, 'archive.txt')

        download_options = {
            'cachedir': 'False',
            'format': 'bestaudio/best',
            'outtmpl': out_path,
            'nocheckcertificate': True,
            'download_archive': archive_file,
            'cookiefile': cookie_file,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

    else:
        download_options = {
            'cachedir': 'False',
            'format': 'bestaudio/best',
            'outtmpl': out_path,
            'nocheckcertificate': True,
            'cookiefile': cookie_file,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

    with youtube_dl.YoutubeDL(download_options) as dl:
        dl.download([link])
