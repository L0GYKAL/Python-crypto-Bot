#Ordres ouverts
def openOrders()
  if exchange.has[‘fetchOrders’]:
    openOders = exchange.fetchOrders()
    return openOders
  
Cancel order:
def cancelOrder(exchenge: ccxt, id: str, symbol: str):
  try:
    exchange.cancelOrder(id, symbol, params)
    retrun str('Order canceled')
  except e: #if there is an error
    retrun e
  #(ex: exchange.cancelOrder(‘123456789’) = exchange.cancelOrder(order id))
  

#Trades terminés
"""
if exchange.has['fetchOrders']:
    since = exchange.milliseconds () - 86400000  # -1 day from now
    # alternatively, fetch from a certain starting datetime
    # since = exchange.parse8601('2018-01-01T00:00:00Z')
    all_orders = []
    while since < exchange.milliseconds ():
        symbol = None  # change for your symbol
        limit = 20  # change for your limit
        orders = await exchange.fetch_orders(symbol, since, limit)
        if len(orders):
            since = orders[len(orders) - 1]['timestamp']
            all_orders += orders
        else:
            break"""
