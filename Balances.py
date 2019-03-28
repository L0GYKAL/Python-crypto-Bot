# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:47:56 2019

@author: LOGYKAL
"""

# THIS WORKS
import ccxt
import pandas as pd
import requests


def fetchAddress(symbol, address):  # fetchAddress('doge', 'DSFi6NPHgt3R8Jr2HJyrSq35QtuRsUEGxm')
    """ Il faut faire une liste défilante avec les asset qui sont retournés par la request ci-dessus
    symbolList = requests.get('https://api.hybrix.io/asset/').json()"""
    request = requests.get(
        'https://api.hybrix.io/asset/' + symbol + '/balance/' + address).json()
    if request['error'] == 0:
        balance = requests.get(
            'https://api.hybrix.io/proc/' + str(request['data'])).json()
        return balance['data']
    else:
        print('There is a probleme')


def convertAdress(symbol: str, amount: float, conversion: str) -> float:
    """symbol: BTC
    amount:0.25968
    conversion: EUR"""
    request = requests.get('https://api.cryptonator.com/api/full/' + symbol + '-' + conversion)
    weightedPrice= request['ticker']['price']
    return weightedPrice


def fetchExchangeBalance(exchange):
    total=float()
# exchange[0]=ccxtObject and exchange[1]=name
    """binance = ccxt.binance({
        'id':
        'Binance',
        'apiKey':
        'QDvA3MvcZNgy0kFmsSFlBwX3VirMcV5VnhjOctTRqohH46Ces8glcRys48H8ddwX',
        'secret':
        'yISA8ODctEZY4ncjpHIxAKar638Xe9hvjmldi7TRKxQ9L1Zcb3MvSuJMDpeIG8rs'
    })"""
    balances=exchange[0].fetchBalance()
    # print(balances)
    balances=pd.DataFrame(data=balances['info']['balances'])
    markets = exchange[0].loadMarkets()
    for i in balances.index:
        ticker=balances.loc[i, 'asset'] + '/BTC'
            if exchange[0].markets[ticker]:
                if float(balances.loc[i, 'free']) + float(
                        balances.loc[i, 'locked']) != 0:
                    if balances.loc[i, 'asset'] == 'BTC':
                        balInBTC=float(balances.loc[i, 'free']) + float(
                            balances.loc[i, 'locked'])
                    else:
                        if markets[ticker] != 0:
                            balInBTC=ticker['last'] * (
                                float(balances.loc[i, 'free']) + float(balances.loc[i, 'locked']))
            print('You have ' + str(
                float(balances.loc[i, 'free'])
                + float(balances.loc[i, 'locked'])
            ) + ' ' + balances.loc[i, 'asset'] + ' It represents ' + str(balInBTC))
            total += balInBTC
    print('You have an approximate amount of'
          + total + ' BTC in ' + exchange[1])
