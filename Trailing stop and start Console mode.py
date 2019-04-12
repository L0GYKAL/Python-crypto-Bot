import ccxt
import asyncio

async def trailingStop(symbol, exchange, amount):
    lastHigh = 0
    sold = False
    prices = stopLossPrice(exchange, lastHigh, percent=3, symbol)
    while sold != True:
        prices = stopLossPrice(exchange, prices[1], percent=3, symbol)
        if get_lastPrice(symbol, exchange) < stopLossPrice:
            sold = marketSell(exchange, symbol, amount)
            await asyncio.sleep(15)

# Get the last price


def get_lastPrice(symbol, exchange):
    Ticker = exchange.fetch_ticker(symbol)
    return Ticker['last']  # return lastPrice


# Trailing

#get a price
def stopLossPrice(exchange, lastHigh, percent=3, symbol='USDT/BTC'):
    lastPrice = get_lastPrice(symbol, exchange)
    if lastPrice > lastHigh:  # si le dernier prix est supérieur au plus haut récent alors le plus haut récent devient le dernier prix
        lastHigh = lastPrice
    stopLossPrice = lastHigh-(lastHigh/100*percent)
    return [stopLossPrice,lastHigh]


def startBuyPrice(exchange, lastLow, percent=3, symbol='USDT/BTC'):
    lastPrice = get_lastPrice(symbol, exchange)
    if lastPrice < lastLow:  # si le dernier prix est inférieur au plus bas récent alors le plus bas récent devient le dernier prix
        lastLow = lastPrice
    startBuyPrice = lastLow+(lastLow/100*percent)
    return [startBuyPrice,lastLow]

def marketSell(exchange, symbol, amount):
    orderBook = exchange.fetch_l2_order_book(symbol)
    i=0
    while amount !=0:
        i+=1
        if orderbook['bids'][i][1]>amount:
            exchange.createLimitSellOrder (symbol, orderbook['bids'][i][1], orderbook['bids'][i][0])
            amount-=orderbook['bids'][i][1]
        else:
            exchange.createLimitSellOrder (symbol, amount, orderbook['bids'][i][0])
            amount=0
    return True

"""
loop = asyncio.get_event_loop()
loop.create_task(trailingStop(symbol, exchange, amount))
loop.run_forever()
loop.close()

"""
