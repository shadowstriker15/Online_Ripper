import youtube_dl
from pathlib import Path
import datetime


# Download data and config

file_path = "C:/Users/austi/Downloads/%(title)s.%(ext)s"

download_options = {
    'format': 'bestaudio/best',
    'outtmpl': file_path,
    'nocheckcertificate': True,
    'download_archive': 'archive.txt',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
song_url = "https://www.youtube.com/playlist?list=PLl3Ghld2faMaoRei6-Fe5LAegMfb91yEg"

path = "Users/austi/Downloads"

date = datetime.date.today()


def yt_download(link):
    # if file_path != "":
    # home = str(Path.home())
    # file_path = home
    # file_path = file_path + '\%(title)s.%(ext)s'
    with youtube_dl.YoutubeDL(download_options) as dl:
        dl.download([link])
