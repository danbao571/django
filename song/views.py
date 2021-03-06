from io import BytesIO
import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .ku_api import Search
from django.conf import settings
import json
from rest_framework.views import APIView
from djpjax import pjax, PJAXResponseMixin


class MusicView(PJAXResponseMixin, APIView):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return render(request, 'song/music.html', locals())
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
    data = {}
    if not file:
        msg = '请选择图片文件'
        data['msg'] = msg
        return JsonResponse(data)
    search = Search()
    result = search.remove(file)
    path = settings.SHOW_ROOT + '\\remove\\%s' % file.name
    with open(path, "wb") as f:
        f.write(result)
    data['img'] = 'http://127.0.0.1:8000/static/remove/%s' % file.name
    return JsonResponse(data)


def download_music(request):
    song = request.GET.get('src', None)
    response = HttpResponse(content_type='audio/mpeg')
    re = requests.get(song).content
    output = BytesIO()
    output.write(re)
    response.write(output.getvalue())
    return response
