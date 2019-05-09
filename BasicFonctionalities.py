import requests
import ccxt
import pandas as pd
import tweepy  # wrapper api de tweeter # https://developer.twitter.com/en/docs.html
# module d'analyse sentimental
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def getAllCurrencies():  # return all symbols of the most known cryptocurrencies
    response = requests.get(
        url='https://api.coinmarketcap.com/v1/ticker/').json()
    currencies = []
    for currency in response:
        currencies.append(currency['symbol'])
    return currencies


def is_connected():  # retrun True if connected, False else
    url = 'http://www.google.com/'
    timeout = 5
    try:
        # connect and tell us if the host is reachable
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("İnternet bağlantısı yok.")
    return False


def tickerFinder(symbol: str):
    markets = dict()
    certified = ['upbit', 'kucoin', 'kraken',
                 'coss', 'bittrex', 'bitfinex', 'binance']
    ccxtList = []
    for exchange in certified:
        exec("ccxtList.append(ccxt." + str(exchange) + "())")
    for exchange in certified:  # ticker in certified[exchange]...
        i = 0
        # trouver tous les tickers
        markets[exchange] = ccxtList[i].loadMarkets()
        i += 1
    for exchange in certified:
        tickers = []
        for ticker in markets[exchange].keys():
            if str(ticker).find(symbol) != -1:
                tickers.append(str(ticker))
        markets[exchange] = tickers
    return markets


def marketPercent():
    # récupération des informations ar API
    info = requests.get('https://api.coinmarketcap.com/v1/ticker/').json()
    percentages = []
    # 7days
    percentage7d = float()
    totalpercent = float()
    for i in info:
        totalpercent += float(i['percent_change_7d'])
    # division de la somme des pourcentages par toute les crypto
    percentage7d = totalpercent / len(info)
    # ajout à la liste du pourcentage arrondie
    percentages.append(round(percentage7d, 4))
    # 1day
    percentage1d = float()
    totalpercent = float()
    for i in info:
        totalpercent += float(i['percent_change_24h'])
    percentage1d = totalpercent / len(info)
    # ajout à la liste du pourcentage arrondie
    percentages.append(round(percentage1d, 4))
    # 1hour
    percentage1h = float()
    totalpercent = float()
    for i in info:
        totalpercent += float(i['percent_change_1h'])
    percentage1h = totalpercent / len(info)
    # ajout à la liste du pourcentage arrondie
    percentages.append(round(percentage1h, 4))
    # liste avec la moyenne des porncentages sur 7 jours, sur 24 heures et sur une heure
    return percentages


def sentimentAnalysis(symbol: str)-> list:  # ex: symbol = BTC
    # My Twitter API Authentication Variables
    consumer_key = 'KWp3yqhwWdp0Fn9AcHx58878E'
    consumer_secret = 'ABjkYLIDcc94MMQqQaCZ7eyrFkkoHiFpijRCjN7T3DfOuFb0JG'
    access_token = '2210545440-qoCIdDpU5k7HSNzC3Kz2LDMmOgGMWrotTwkq4qy'
    access_token_secret = 'P8J4IRpOPRXgskDTRCNGw94A6OJ0iA2ORBAJJOvFJ8LLG'

    # authentification
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # récupération des tweets
    tweets = api.search(str('$' + symbol), count=200)

    # création d'un dataframe avec les tweets
    data = pd.DataFrame(
        data=[tweet.text for tweet in tweets], columns=['Tweets'])
    sid = SentimentIntensityAnalyzer()
    sentiments = []

    for index, row in data.iterrows():
        ss = sid.polarity_scores(row["Tweets"])
        sentiments.append(ss)

    se = pd.Series(sentiments)
    data['polarity'] = se.values
    return data['polarity']


if __name__ == '__main__':
    if is_connected():
        print(tickerFinder('OMG'))
