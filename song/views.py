from io import BytesIO
import requests
import xlwt
from django.contrib.auth.decorators import login_required
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
    result = request.path.find('?')
    print(result)
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
    # print('hhh')
    # data_info = [
    #     {
    #         "name": "瓷砖",
    #         "price": 15.5,
    #         "num": 1500.0,
    #         "unit": "个"
    #     },
    #     {
    #         "name": "撒旦撒旦撒",
    #         "price": 0.0,
    #         "num": 453.0,
    #         "unit": "个"
    #     },
    #     {
    #         "name": "辣翻天",
    #         "price": 0.0,
    #         "num": 453.0,
    #         "unit": "条"
    #     }
    # ]
    # name = '刘永杰好帅啊我叼！'
    # response = HttpResponse(content_type='application/vnd.ms-excel')
    # response['Content-Disposition'] = f'attachment;filename={name}.xls'
    # wb = xlwt.Workbook(encoding='utf-8')
    # w = wb.add_sheet('sheet1')
    # w.write(0, 0, '排名')
    # w.write(0, 1, '商品名称')
    # w.write(0, 2, '采购单价')
    # w.write(0, 3, '当前库存')
    # row = 1
    # for data in data_info:
    #     num = data_info.index(data)
    #     name = data['name']
    #     price = data['price']
    #     kc_num = data['num']
    #     unit = data['unit']
    #     w.write(row, 0, num)
    #     w.write(row, 1, name)
    #     w.write(row, 2, price)
    #     w.write(row, 3, f'{kc_num}{unit}')
    #     row += 1
    # output = BytesIO()
    # wb.save(output)
    # # output.seek(0)
    # response.write(output.getvalue())
    # print(response, type(response))
    # return response


def download_music(request):
    song = request.GET.get('src', None)
    response = HttpResponse(content_type='audio/mpeg')
    re = requests.get(song).content
    output = BytesIO()
    output.write(re)
    response.write(output.getvalue())
    return response
