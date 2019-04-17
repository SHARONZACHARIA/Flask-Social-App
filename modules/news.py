

import requests,json

def getNews():
    try:
        url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=APIKEY'
        response = requests.get(url)
        datas = response.json()
        return datas['articles']
    except:
        return ''
    

    
    
