# b1701105e13e42668eb9d08a9a976920

import requests,json

def getNews():
    try:
        url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=b1701105e13e42668eb9d08a9a976920'
        response = requests.get(url)
        datas = response.json()
        return datas['articles']
    except:
        return ''
    

    
    