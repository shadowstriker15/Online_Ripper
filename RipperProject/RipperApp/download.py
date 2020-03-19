import youtube_dl
# from tkinter import filedialog
# from tkinter import *
from pathlib import Path

# Download data and config
download_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'download_archive': 'archive.txt',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
song_url = "https://www.youtube.com/playlist?list=PLl3Ghld2faMaoRei6-Fe5LAegMfb91yEg"


def youtube(self, link):
    # print(link)
    # root = Tk()
    # root.withdraw()
    # folder_selected = filedialog.askdirectory()
    # print(folder_selected)
    home = str(Path.home())
    print(home)
    file_path = home
    file_path = file_path + '\%(title)s.%(ext)s'
    # print(file_path)
    # if file_path != "":
    with youtube_dl.YoutubeDL(download_options) as dl:
        dl.download([link])
