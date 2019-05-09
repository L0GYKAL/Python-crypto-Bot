import ccxt

#Ordres ouverts
def openOrders(exchange: ccxt):
    if exchange.has['fetchOpenOrders']:
        exchange.options["warnOnFetchOpenOrdersWithoutSymbol"] = False
        openOders = []
        orders = exchange.fetchOpenOrders()
        for openOrder in orders:
            openOders.append([openOrder['id'], openOrder['symbol'], openOrder['side'], openOrder['price'], openOrder['amount']])
        return openOders#liste de liste [id, symbol, SELL/BUY, price, amount]

#Cancel order:
def cancelOrder(exchange: ccxt, orderId, symbol: str): #ex: cancelOrder(binance, 11480381, 'MFT/BTC')
  try:
    exchange.cancelOrder(orderId, symbol)
    return str('Order canceled')
  except: #if there is an error
    print('error')
  #(ex: cancelOrder(binance, 11480381, 'MFT/BTC'))
  
#créer un ordre
def createOrder(exchange: ccxt, symbol: str, amount: float, price: float, side: str, type: str):# (side= 'buy' or 'sell'), type = 'limit' or 'market'
    #binance.create_order('RVN/BTC', 'limit', 'buy', amount = 1.0, price = 0.060154)
    order = exchange.create_order(symbol, type, side, amount, price)
    return order