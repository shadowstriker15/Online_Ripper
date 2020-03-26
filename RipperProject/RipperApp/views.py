from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.urls import reverse
import os
import glob
from .download import yt_download
from .edit_song import editor
from .models import Link, Song, Document
from .forms import RawLinkForm, RawSongForm, DocumentForm


def home_view(request):
    link_form = RawLinkForm()
    context = {
        'link_form': link_form
    }

    # Handle file upload
    if request.method == 'POST':

        link_form = RawLinkForm(request.POST)
        if link_form.is_valid():
            Link.objects.create(**link_form.cleaned_data)
            link = link_form.cleaned_data['link']
            yt_download(link)

    return render(request, 'RipperApp/index.html', context)


def song_edit_view(request):
    form = RawSongForm()
    context = {
        'form': form
    }

    path_list = glob.glob("C:\\Users\\austi\\Desktop\\Hello\\*.mp3")
    file_list = []
    for path in path_list:
        file_name = os.path.basename(path)
        file_list.append(file_name)
    context.update({"path_list": path_list})
    file_name = file_list[0]
    # context.update({"file_list": file_list})
    context.update({"file_name": file_name})
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
            editor(artist, title, album, path_list)
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


# def progress(request):
#     pass


# def progress_view(request):
#     print("In view")
#     result = my_task.delay(10)
#     # print(result.task_id, "This is task id in view")
#     return render(request, 'RipperApp/display_progress.html', context={'task_id': result.task_id})


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request, 'RipperApp/list.html', {'documents': documents, 'form': form})
