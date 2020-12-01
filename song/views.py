from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from .ku_api import Search
from django.conf import settings
import json


def music(request):
    return render(request, 'song/music.html', locals())


def search_song(request):
    q = request.GET.get('word')
    data = {}
    if not q:
        data['status'] = 'SPACE'
    else:
        par = q.split(' ')
        name = par[0]
        page = par[1] if len(par) > 1 else 1
        search = Search()
        result = search.get_rid(name, page)
        data['status'] = "SUCCESS"
        data['info'] = result
    return JsonResponse(data)


def get_song_url(request):
    rid = request.GET.get('rid')
    search = Search()
    song_info = search.get_url(rid)
    song_url = json.loads(song_info)
    data = {}
    data['info'] = song_url
    return JsonResponse(data)


def remove_bg(request):
    file = request.FILES.get('photo', None)
    search = Search()
    result = search.remove(file)
    path = settings.SHOW_ROOT + '\\remove\\%s' % file.name
    with open(path, "wb") as f:
        f.write(result)
    data = {}
    data['img'] = 'http://127.0.0.1:8000/static/remove/%s' % file.name
    return JsonResponse(data)
