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
    filename = str(ticker).replace('/', ' ') + '.html'
    plot = py.plot(fig, filename=filename, auto_open=False)
    return plot


if __name__ == '__main__':
    #binance = ccxt.binance()
    chart(binance, 'RVN/BTC', '1d')
