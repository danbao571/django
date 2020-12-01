# -*- coding:utf-8 -*-
import requests
import json


class Search(object):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Host': 'www.kuwo.cn',
        'Connection': 'keep-alive',
        'Cookie': 'kw_token=MTZQZ7M2J5D; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1594628502;'
                  ' Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1594633393; '
                  '_ga=GA1.2.2022098415.1594628503; _gid=GA1.2.152069903.1594628503; _gat=1',
        'Referer': 'http://www.kuwo.cn/search/list',
        'CSRF': 'MTZQZ7M2J5D'
    }

    def get_rid(self, name, page):
        url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}' \
              '&pn={}&rn=100&httpsStatus=1&reqId=9a1ff3e0-c4ed-11ea-9548-17f87347f6a3'.format(name, page)
        response = requests.get(url, headers=self.headers).content.decode()
        info_list = json.loads(response)["data"]["list"]
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

    def remove(self, file):
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': file},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'RLgXtt1EywEE28Xusa7BWUQ3'},
        )
        return response.content
