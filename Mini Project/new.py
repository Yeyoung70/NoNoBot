import requests
import json
import pandas as pd

import email
import smtplib

def datas_a():
    URL = 'https://api.stunning.kr/api/v1/dantats/portfolio?state=Public&limit=20&category=portfolio.category.katiethompson&orderBy=pick&pick=Y'
    response = requests.get(URL, headers={
    'X-Service-Clause': 'notefolio'})
    Design_tags = json.loads( response.text )

    details_URL = 'https://notefolio.net/spangles/'
    datas = []
    for Design in Design_tags['resultData'][:7]:
        a = 'categories'
        if Design['user'].get(a, 0):
            b = 'description'
            if Design['user']['userProfile'].get(b, 0):
                datas.append({
                    '이미지': Design['cover']['url'],
                    '제목': Design['title'],
                    '디자이너': Design['user']['nick'],
                    '태그': Design['user']['categories'][0]['tag'],
                    '프로필': Design['user']['userProfile']['description'],
                    '링크' : details_URL +  str(Design['id']),
                })

    columns = ','.join(datas[0].keys())
    columns = ['이미지', '제목', '디자이너', '태그', '프로필', '링크']
    values = []
    for data in datas[:7]:
        values.append(tuple(data.values()))

    b = []
    for data in datas:
        b.append( '[\t'+ data['제목'] + '\t]' +'\n'
        + '\n'
        + data['프로필'] + '\n'
        + data['링크'] + '\n') 
        
    return b
    pass
