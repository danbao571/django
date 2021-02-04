# -*- coding:utf-8 -*-
import requests
import json
from uuid import uuid4
import base64


class Search(object):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Host': 'www.kuwo.cn',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1612410008;'
                  ' _ga=GA1.2.161966496.1604580196; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1612410008; '
                  'kw_token=D8U0ZU7D7FA; _gid=GA1.2.1214265788.1612410009; _gat=1',
        'Referer': 'http://www.kuwo.cn/search/list',
        'CSRF': 'D8U0ZU7D7FA'
    }

    def get_rid(self, name, page):
        url = f'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={name}&pn={page}' \
              f'&rn=100&reqId={uuid4()}'
        response = requests.get(url, headers=self.headers).json()
        info_list = response["data"]["list"]
        return info_list

    def get_url(self, rid):
        url = 'https://kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3' \
              '&br=128kmp3&from=web&t=1605229999897&httpsStatus=1&' \
              'reqId=6ac5a7a0-254d-11eb-8db8-17eb9e54b690'.format(rid)
        response = requests.get(url).content.decode()
        return response

    def get_ci(self, rid):
        url = 'https://player.kuwo.cn/webmusic/st/getNewMuiseByRid?rid={}'.format(rid)
        response = requests.get(url).content.decode('utf-8')
        return response

    def download_music(self, src, name):
        song = requests.get(src).content
        with open(name + '.mp3', 'wb') as f:
            f.write(song)
        return 'SUCCESS'

    def remove(self, file):
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': file},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'RLgXtt1EywEE28Xusa7BWUQ3'},
        )
        return response.content
