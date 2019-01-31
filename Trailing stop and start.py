# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:46:51 2019

@author: LOGYKAL
"""
import ccxt

# Get the last price


def get_lastPrice(symbol, exchange):
    Ticker = exchange.fetch_ticker(symbol)
    return Ticker['last']  # return lastPrice


# Trailing


def stopLossPrice(exchange, lastHigh, percent=3, symbol='USDT/BTC'):
    lastPrice = get_lastPrice(symbol, exchange)
    if lastPrice > lastHigh:  # si le dernier prix est supérieur au plus haut récent alors le plus haut récent devient le dernier prix
        lastHigh = lastPrice
    stopLossPrice = lastHigh-(lastHigh/100*percent)
    return stopLossPrice


def startBuyPrice(exchange, lastLow, percent=3, symbol='USDT/BTC'):
    lastPrice = get_lastPrice(symbol, exchange)
    if lastPrice < lastLow:  # si le dernier prix est inférieur au plus bas récent alors le plus bas récent devient le dernier prix
        lastLow = lastPrice
    startBuyPrice = lastLow+(lastLow/100*percent)
    return startBuyPrice

def MarketSell(exchange, symbol, amount):
    orderBook = exchange.fetch_l2_order_book(symbol)
    i=0
    while amount !=0:
        i+=1
        if orderbook['bids'][i][1]>amount:
            #Limit_order (    price=orderbook['bids'][i][0],    amount_of-this-order=orderbook['bids'][i][1])
            amount-=orderbook['bids'][i][1]
        else:
            #Limit_order (    price=orderbook['bids'][i][0],    amount_of-this-order=amount)
            amount=0
        

def StopOrder(stopLossPrice,exchange,symbol): #teste si le stoploss a été dépassé ou non => "if last<stoploss and bid/last*100<percent" (que pour startgain)





"""

    import asyncio
    import os
    import sys

    if not sys.version >= '3.6':
        print('This script requires Python 3.6+')
        sys.exit()   
    
    
    """



