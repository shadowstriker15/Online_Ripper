import os
import glob
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Link, Song
from .forms import RawLinkForm, RawSongForm
from pathlib import Path
from .download import yt_download
from .get_cover import find_cover
from .edit_song import editor
from .find_album import get_album


def home_view(request, account_name=None):
    if not request.user.is_authenticated:
        messages.info(request, f'Please register or login to download')
    current_user = request.user
    link_form = RawLinkForm()
    context = {
        'link_form': link_form
    }

    if request.method == 'POST':

        link_form = RawLinkForm(request.POST)
        if link_form.is_valid():
            if not request.user.is_authenticated:
                messages.error(request, f'You must be logged in to download')
            else:
                Link.objects.create(**link_form.cleaned_data)
                link = link_form.cleaned_data['link']
                yt_download(link, current_user)
                messages.info(request, f"Download complete! Click 'Continue'")
        else:
            context.update({'link_form': link_form})

    return render(request, 'RipperApp/index.html', context)


def song_edit_view(request):
    song_form = RawSongForm()
    context = {
        'song_form': song_form,
        'path_num': 1,
    }
    current_user = request.user
    user = str(current_user)

    file_list = get_song_list(request)
    path_list = get_path_list(request)

    # Check to see if any downloaded mp3s
    if len(path_list) != 0:
        file_name = file_list[0]
        context.update({"file_name": file_name})
    else:
        context.update({'path_num': 0})
        messages.info(request, f'No more new downloaded songs')

    if request.method == "POST":
        song_form_post = RawSongForm(request.POST)

        if song_form_post.is_valid():
            artist = song_form_post.cleaned_data['artist']
            title = song_form_post.cleaned_data['title']
            genre = song_form_post.cleaned_data['genre']

            album, cover_link = get_album(artist, title)

            if album == "Invalid":
                album = None
                messages.error(request, f'Could not set album name and cover')
                album_path = None
            else:
                album_path = find_cover(cover_link, user)

            editor(artist, title, album, genre, path_list, album_path)
            Song.objects.create(**song_form_post.cleaned_data)

            response = HttpResponse(open(path_list[0], 'rb').read())
            response['Content-Type'] = 'audio/mpeg'
            file_name = title + '.mp3'
            response['Content-Disposition'] = "attachment; filename=\"" + file_name + "\""
            return response

    return render(request, 'RipperApp/song_edit.html', context)


# Used to find mp3s in user's Downloads
def get_path_list(request):
    home = str(Path.home())
    user = str(request.user)
    path = os.path.join(home, 'Users', user, 'Downloads', '*mp3')
    return glob.glob(path)


# Used to get file names
def get_song_list(request):
    path_list = get_path_list(request)
    file_list = []
    for path in path_list:
        file_name = os.path.basename(path)
        file_list.append(file_name)
    return file_list


def next_page(request):
    path_list = get_path_list(request)

    # Check if there is a next song
    if len(path_list) == 1:
        os.remove(path_list[0])
    else:
        os.remove(path_list[0])
    return song_edit_view(request)


# Used to prevent next_page getting called
def download_view(request):
    return song_edit_view(request)


def about_view(request):
    return render(request, 'RipperApp/about.html')
