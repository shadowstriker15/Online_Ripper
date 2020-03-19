from django.shortcuts import render
from django.http import HttpResponse
from .models import Link
from .forms import RawLinkForm
# from .download import youtube


# Create your views here.

def home_view(request):
    return render(request, 'RipperApp/index.html', {})


def link_detail_view(request):
    obj = Link.objects.get(id=3)
    context = {
        'object': obj
    }
    return render(request, 'RipperApp/detail.html', context)


def link_create_view(request):
    form = RawLinkForm()
    if request.method == "POST":
        form = RawLinkForm(request.POST)
        if form.is_valid():
            Link.objects.create(**form.cleaned_data)
    context = {
        'form': form
    }
    # youtube(form)
    return render(request, 'RipperApp/link_create.html', context)
