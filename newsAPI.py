import requests  # api
from bs4 import BeautifulSoup  # parser html


def getNews():  # recupère les news par API et créer une liste de liste avec les informations comme le titre, le corps, la source et la date
    response = requests.get('https://data.messari.io/api/v1/news').json()
    articles = list()
    for news in response['data']:
        try:
            title = BeautifulSoup(news['title'], "html.parser").get_text()
        except:
            title = "None"
        try:
            content = BeautifulSoup(news['content'], "html.parser").get_text()
        except:
            content = "None"
        try:
            source = news['references'][0]['url']
        except:
            news = "None"
        try:
            date = BeautifulSoup(news['published_at'],
                                 "html.parser").get_text()
        except:
            date = "None"
        articles.append([title, content, source, date])

    return (articles)
