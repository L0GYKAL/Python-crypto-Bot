# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:47:56 2019

@author: LOGYKAL
"""

# THIS WORKS
import ccxt
import pandas as pd
import requests
import datetime
import os

balanceHistory = pd.Dataframe()


def getAllSymbols():#tous les symboles de d'adresse de cryptomonnaies supportés par l'API hybrix
    symbolsList = requests.get('https://api.hybrix.io/asset/').json()['data']
    return symbolsList

# timeUnit = 7d or 1h or 24h #rend le pourcentage de différence de prix pour les 100 premières crypto
def marketPercent(timeUnit: str):
    info = requests.get('https://api.coinmarketcap.com/v1/ticker/').json()
    totalpercent7D = float()
    percent = 'percent_change_' + timeUnit
    for i in info.len():
        totalpercent += float(info[i][percent='percent_change_' + timeUnit])
    totalpercent = totalpercent / info.len()
    # print('In 7 days, top 100 cryptocurrencies performed '+ str(totalpercent7D) + '%!')
    return totalpercent


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


def convertAdress(symbol: str, conversion: str) -> float:
    """symbol: BTC
    conversion: EUR"""
    request = requests.get(
        'https://api.cryptonator.com/api/full/' + symbol + '-' + conversion)
    weightedPrice = request['ticker']['price']
    return weightedPrice


def fetchExchangeBalance(exchange):
    total = float()
# exchange[0]=ccxtObject and exchange[1]=name
    """binance = ccxt.binance({
        'id':
        'Binance',
        'apiKey':
        'QDvA3MvcZNgy0kFmsSFlBwX3VirMcV5VnhjOctTRqohH46Ces8glcRys48H8ddwX',
        'secret':
        'yISA8ODctEZY4ncjpHIxAKar638Xe9hvjmldi7TRKxQ9L1Zcb3MvSuJMDpeIG8rs'
    })"""
    balances = exchange[0].fetchBalance()
    # print(balances)
    balances = pd.DataFrame(data=balances['info']['balances'])
    markets = exchange[0].loadMarkets()
    for i in balances.index:
        ticker = balances.loc[i, 'asset'] + '/BTC'
            if exchange[0].markets[ticker]:
                if float(balances.loc[i, 'free']) + float(
                        balances.loc[i, 'locked']) != 0:
                    if balances.loc[i, 'asset'] == 'BTC':
                        balInBTC = float(balances.loc[i, 'free']) + float(
                            balances.loc[i, 'locked'])
                    else:
                        if markets[ticker] != 0:
                            balInBTC = ticker['last'] * (
                                float(balances.loc[i, 'free']) + float(balances.loc[i, 'locked']))
           """ print('You have ' + str(
                float(balances.loc[i, 'free'])
                + float(balances.loc[i, 'locked'])
            ) + ' ' + balances.loc[i, 'asset'] + ' It represents ' + str(balInBTC))"""
            total += balInBTC
    """print('You have an approximate amount of'
          + total + ' BTC in ' + exchange[1])"""
    return total

def compileBalances():
    #
    for address in adresses:
        try:
            totalBTC += float(fetchAddress(symbol, address)) * \
                float(convertAdress(symbol, 'BTC'))
        except:
            pass
    for exchange in exchanges:
        try:
            totalBTC += float(fetchExchangeBalance(exchange))
        except:
            pass
    return totalBTC


def saveBalance(totalBTC):
    row = [datetime.today(), totalBTC]
    if os.path.isfile('balanceHistory.csv'):
        with open('balanceHistory.csv', 'r') as f:
            balanceHistory = pd.read_csv(f)
        if balanceHistory.at[0, -1] != datetime.today():
            balanceHistory.append(row)
            balanceHistory.to_csv('balanceHistory.csv')
        else:
            pass
    else:
        f = open('balanceHistory.csv', 'a')
        f.close()
        balanceHistory = pd.DataFrame(columns=['date', 'BalanceInBTC'])
        balanceHistory.append(row)
        balanceHistory.to_csv('balanceHistory.csv')


def readBalances():
    if os.path.isfile('balanceHistory.csv'):
        with open('balanceHistory.csv', 'r') as f:
            balanceHistory = pd.read_csv(f)
        return balanceHistory
    else:
        f = open('balanceHistory.csv', 'a')
        f.close()
        balanceHistory = pd.DataFrame(columns=['date', 'BalanceInBTC'])
        balanceHistory.to_csv('balanceHistory.csv')


class addresses:
    def addressExist(id, address, symbol):
        global addressesDf
        for i in addressesDf.index():
            if ((addressesDf.loc[i, 'id'] == id) or (addressesDf.loc[i, 'address'] == address and addressesDf.loc[i, 'symbol'] == symbol)):
                return True
        return False

    def add_Address(self, id, address, symbol):
        global addressesDf
        if addressExist(id, address, symbol):
            print('This address already exist. Try to edit it')
        else:
            addressesDf.append([id, address, symbol])

    def readAddresses():
        global addressesDf
        if os.path.isfile('addresses.csv'):
            with open('addresses.csv', 'r') as f:
                addressesDf = pd.read_csv(f)
        else:
            f = open('addresses.csv', 'a')
            f.close()
            balanceHistory = pd.DataFrame(columns=['id', 'address', 'symbol'])
            balanceHistory.to_csv('addresses.csv')
