from django.shortcuts import render
from . import models

def index(request):
    lyrics = models.Lyric.objects.all()
    context  = {
        "lyrics": lyrics
    }
    return render(request, 'musics/index.html', context)
   

def details(request, music_id):
    context = {
        "lyric": models.Lyric.objects.get(pk=music_id)
    }
    return render(request,'musics/details.html', context)
