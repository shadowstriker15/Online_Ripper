from django import forms
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.urls import reverse
import os
import glob
from .download import yt_download
from .get_album import get_album
from .edit_song import editor
from .models import Link, Song
from .forms import RawLinkForm, RawSongForm
from django.contrib import messages
from pathlib import Path


def home_view(request, account_name=None):
    if not request.user.is_authenticated:
        messages.info(request, f'Please register or login to download.')
    current_user = request.user
    link_form = RawLinkForm()
    context = {
        'link_form': link_form
    }
    # if not account_name:
    #     error = 'Create or sign into an account'
    #     context.update({'error': error})

    if request.method == 'POST':

        link_form = RawLinkForm(request.POST)
        if link_form.is_valid():
            if not request.user.is_authenticated:
                messages.error(request, f'You must be logged in to download.')
            else:
                Link.objects.create(**link_form.cleaned_data)
                link = link_form.cleaned_data['link']
                yt_download(link, current_user)
                messages.info(request, f'Download complete!')

    return render(request, 'RipperApp/index.html', context)


def song_edit_view(request):
    form = RawSongForm()
    context = {
        'form': form
    }
    current_user = request.user
    home = str(Path.home())
    user = str(current_user)

    path = os.path.join(home, 'Users', user, 'Downloads', '*mp3')
    path_list = glob.glob(path)
    file_list = []
    for path in path_list:
        file_name = os.path.basename(path)
        file_list.append(file_name)

    context.update({"path_list": path_list})
    print(file_list, "this is file list")
    if len(file_list) != 0:
        file_name = file_list[0]
        context.update({"file_name": file_name})
    else:
        messages.info(request, f'No more new downloaded songs.')

    if request.method == "POST":

        # doc_form = DocumentForm(request.POST, request.FILES)
        #
        # context.update({'doc_form': doc_form})

        song_form = RawSongForm(request.POST)

        # if doc_form.is_valid():
        #     new_doc = Document(docfile=request.FILES['docfile'])
        #     new_doc.save()

        if song_form.is_valid():
            artist = song_form.cleaned_data['artist']
            title = song_form.cleaned_data['title']
            album = song_form.cleaned_data['album']
            genre = song_form.cleaned_data['genre']
            album_path = get_album(album, user)
            editor(artist, title, album, genre, path_list, album_path)
            Song.objects.create(**song_form.cleaned_data)
            # real_download(request, path_list[0])
            response = HttpResponse(open(path_list[0], 'rb').read())
            response['Content-Type'] = 'audio/mpeg'
            file_name = str(file_name)
            response['Content-Disposition'] = "attachment; filename=\"" + file_name + "\""
            os.remove(path_list[0])
            return response

    return render(request, 'RipperApp/song_edit.html', context)


def real_download(request, path=None):
    # if path is None:
    #     raise Http404
    # else:
    # path = path.replace(os.sep, "/")
    # print(path)
    response = HttpResponse(open(path, 'rb').read())
    response['Content-Type'] = 'audio/mpeg'
    response['Content-Disposition'] = 'attachment; filename=DownloadedSong.mp3'
    # os.remove(path_list[0])
    return response


def next_page(request):
    # Clicked next button
    # if request.GET.get('next'):
    #     pass
    return song_edit_view(request)


def about_view(request):
    return render(request, 'RipperApp/about.html')
