# Online_Ripper
A Repository for a Django YouTube Ripper

## About
To see this repository in action, check out my website, [Song Ripper](http://shadowstriker15.pythonanywhere.com).

This project was made possible from these Python modules:
* [youtube_dl](https://youtube-dl.org/)
* [spotipy](https://spotipy.readthedocs.io/en/2.9.0/)
* [eyed3](https://eyed3.readthedocs.io/en/latest/)

And from the great open [Spotify API](https://developer.spotify.com/documentation/web-api).

## Main Functionalities

* Online Ripper can be used to rip audio from YouTube videos from a provided link to create a downloadable mp3 file.

* While downloading the file, Online Ripper can modify the mp3's metadata to include *Artist*, *Title*, and *Genre*

* Online Ripper can retrieve and set the album cover based on the artist name and title.

A key feature included, using youtube_dl's handy archive function, is providing a user-made playlist and only downloading newly added videos based on server-side record keeping.

## User Guide

1. Insert a valid YouTube link of your **public** playlist (or the link to an individual music video)

![Step1](https://user-images.githubusercontent.com/1342626/89725555-65100980-d9d6-11ea-8b41-0a054703a254.png)

2. After the download has completed, click the new *Continue* button above

3. At the next page, you will now be able to edit the metadata of each file. Use the form to fill in the appropriate fields and click *Download* once completed. Click *Next* once you are ready for the next file

![Step2](https://user-images.githubusercontent.com/1342626/89725524-0054af00-d9d6-11ea-9c7d-f29ee6692b72.png)

4. Once you have downloaded all of your files, you will be greeted with this page:

![Step3](https://user-images.githubusercontent.com/1342626/89725537-0f3b6180-d9d6-11ea-92c8-2bbf076afabd.png)

5. You can now return to the homepage and repeat for any new songs added to the playlist

## Extra

For additional information, please visit [Song Ripper](http://shadowstriker15.pythonanywhere.com) and read from the homepage.
