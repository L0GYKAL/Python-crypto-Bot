import socket


def is_connected():  # retrun True if connected, False else
    try:
        # connect and tell us if the host is reachable
        socket.create_connection(‘www.google.com’, 80)
        return True
    except OSError:
        pass
    return False

def tickerFinder(symbol: str):
    markets = dict()
    certified = ['upbit', 'kucoin', 'kraken', 'coss', 'bittrex', 'bitfinex', 'binance']
    ccxtList = []
    for exchange in certified:
        exec("ccxtList.append(ccxt." + str(exchange) + "())")
    for exchange in certified: #ticker in certified[exchange]...
        i=0
        markets[exchange] = ccxtList[i].loadMarkets()#trouver tous les tickers
        i+=1
    for exchange in certified:
        tickers = []
        for ticker in markets[exchange].keys():
            if str(ticker).find(symbol) != -1:
                tickers.append(str(ticker))
        markets[exchange] = tickers
    return markets

if __name__ == '__main__':
    if is_connected():
        print(tickerFinder('OMG'))
