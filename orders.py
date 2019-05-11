import ccxt

#Ordres ouverts
def openOrders(exchange: str, apikey: str, secret: str):
    exec('exchange = ccxt.' + exchange + "({'apikey':" + apikey + "'secret':" + secret + "})" )
    if exchange.has['fetchOpenOrders']:
        exchange.options["warnOnFetchOpenOrdersWithoutSymbol"] = False
        openOders = []
        orders = exchange.fetchOpenOrders()
        for openOrder in orders:
            openOders.append([openOrder['id'], openOrder['symbol'], openOrder['side'], openOrder['price'], openOrder['amount']])
        return openOders#liste de liste [id, symbol, SELL/BUY, price, amount]

#Cancel order:
def cancelOrder(exchange: str, orderId, symbol: str, apikey, secret): #ex: cancelOrder(binance, 11480381, 'MFT/BTC')
    exec('exchange = ccxt.' + exchange + "({'apikey':" + apikey + "'secret':" + secret + "})" )
    try:
        exchange.cancelOrder(orderId, symbol)
        return str('Order canceled')
      except: #if there is an error
        print('error')
      #(ex: cancelOrder(binance, 11480381, 'MFT/BTC'))
  
#créer un ordre
def createOrder(exchange: str, symbol: str, amount: float, price: float, side: str, type: str):# (side= 'buy' or 'sell'), type = 'limit' or 'market'
    #binance.create_order('RVN/BTC', 'limit', 'buy', amount = 1.0, price = 0.060154)
    exec('exchange = ccxt.' + exchange + '()')
    order = exchange.create_order(symbol, type, side, amount, price)
    return order
