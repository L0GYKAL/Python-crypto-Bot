from dateutil.parser import parse
import time
import pandas as pd
import ccxt
import plotly.graph_objs as go
import plotly.offline as py


def chart(exchange: ccxt, ticker: str, time):  # time: '1m','1d'
    df = pd.DataFrame(exchange.fetchOHLCV(ticker, time))
    df[0] = pd.to_datetime(df[0], unit='ms')
    layout = {'title': ticker,
              'yaxis': {'title': 'Price'}}
    trace = go.Candlestick(
        x=df[0],
        open=df[1],
        high=df[2],
        low=df[3],
        close=df[4])
    data = [trace]
    fig = dict(data=data, layout=layout)
    filename = 'plotlyGraph.html'
    plot = py.plot(fig, filename=filename, auto_open=False)
    return plot


def BTC_liveGraph():
    global plot_url  # pour afficher le graph, il faut utiliser cette URL
    # déclaration des constantes
    bitmex = ccxt.bitmex({'enableRateLimit': True})
    layout = {'title': 'BTC live price',
              'yaxis': {'title': 'Price in USD'}}
    filename = 'BTC_liveGraph.html'
    # récupération des premières info
    ticker = bitmex.fetchTicker('BTC/USD')
    datetime = parse(ticker['datetime']).time()
    price = ticker['last']
    # déclaration de la dataframe pandas
    df = pd.DataFrame(columns=['time', 'price'], data=[[datetime, price]])
    # boucle d'update
    while True:
        time.sleep(bitmex.rateLimit * 2 / 1000)  # time.sleep wants seconds
        ticker = bitmex.fetchTicker('BTC/USD')
        datetime = parse(ticker['datetime']).time()
        price = ticker['last']
        df.loc[len(df)] = [datetime] + [price]
        trace = go.Scatter(x=df['time'], y=df['price'])
        data = [trace]
        fig = dict(data=data, layout=layout)
        plot_url = py.plot(fig, filename=filename, auto_open=False)
        
def plotsentimentAnalysis(data: list):#return a url to a graph
    negativScore = float()
    positivScore = float()
    neutralScore = float()
    for score in data:
        positivScore += score['pos']
        negativScore += score['neg']
        neutralScore += score['neu']
        
    trace = {
        "labels": ["Positive", "Negative", "Neutral"],
        "type": "pie",
        "values": [positivScore, negativScore, neutralScore]
    }
    py.iplot([trace], filename='sentimentAnalysis_Pie.html')     


if __name__ == '__main__':
    """binance = ccxt.binance()
    chart(binance, 'RVN/BTC', '1d')"""
    BTC_liveGraph()
