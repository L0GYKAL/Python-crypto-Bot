import requests
def news():
    response = requests.get('https://data.messari.io/api/v1/news').json()
    articles= list()
    for news in response:
        title = response[news]['data']['title']
        content = response[news]['data']['content']
        source = response[news]['data']['references']['url']
        date = response[news]['data']['published_at']
        articles.append(title,content,source,date)
    return articles
