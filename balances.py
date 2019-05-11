import ccxt
import pandas as pd
import requests


def getAllSymbols():  # tous les symboles de d'adresse de cryptomonnaies supportés par l'API hybrix
    symbolsList = requests.get('https://api.hybrix.io/asset/').json()['data']
    return symbolsList


def fetchAddress(symbol, address):  # fetchAddress('btc', '385cR5DM96n1HvBDMzLHPYcw89fZAXULJP')
    """le symbol est à choisir parmis ceux de la liste retournés par getAllSymbols()"""
    request = requests.get(
        'https://api.hybrix.io/asset/' + symbol + '/balance/' + address).json()  # demande le montant de crypto sur cette adresse
    if request['error'] == 0:
        balance = requests.get(
            'https://api.hybrix.io/proc/' + str(request['data'])).json()  # api en deux étapes: deuxième montant
        if balance['data'] == None:
            balance['data'] = 0
        return balance['data']
    else:
        print('There is a probleme')


def getPrice(symbol: str, conversion: str) -> float:  # symbol: 'BTC', conversion: 'EUR'
    request = requests.get(
        'https://api.cryptonator.com/api/full/' + symbol + '-' + conversion).json()
    weightedPrice = request['ticker']['price']
    return float(weightedPrice)


def fetchExchangeBalance(exchange: str):
    apikey = APIkeys_fetching()
    df = apikey.get()
    for i, row in df.iterrows():
        if df.loc[i]['exchange'] == exchange:
            apikey = df.loc[i,'apikey']
            secret = df.loc[i,'secret']
    exec('exchange = ccxt.' + exchange + "({'apikey':" + apikey + "'secret':" + secret + "})" )
    total = float()
    """binance = ccxt.binance({
        'id':
        'Binance',
        'apiKey':
        'QDvA3MvcZNgy0kFmsSFlBwX3VirMcV5VnhjOctTRqohH46Ces8glcRys48H8ddwX',
        'secret':
        'yISA8ODctEZY4ncjpHIxAKar638Xe9hvjmldi7TRKxQ9L1Zcb3MvSuJMDpeIG8rs'
    })"""
    balances = exchange.fetchBalance()
    # print(balances)
    balances = pd.DataFrame(data=balances['info']['balances'])
    markets = exchange.loadMarkets()
    for i in balances.index:
        ticker = balances.loc[i, 'asset'] + '/BTC'
        if exchange.markets[ticker]:
            if float(balances.loc[i, 'free']) + float(
                    balances.loc[i, 'locked']) != 0:
                if balances.loc[i, 'asset'] == 'BTC':
                    balInBTC = float(balances.loc[i, 'free']) + float(
                        balances.loc[i, 'locked'])
                else:
                    if markets[ticker] != 0:
                        balInBTC = ticker['last'] * (
                            float(balances.loc[i, 'free']) + float(balances.loc[i, 'locked']))

        total += balInBTC

    return total
