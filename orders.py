import ccxt
import APIkeys_fetching
from GUI import errorMessage, validationMessage
from PyQt5 import QtCore, QtGui, QtWidgets


#Ordres ouverts
def openOrders(exchange: str):
    apikey = APIkeys_fetching()
    df = apikey.get()
    for i, row in df.iterrows():
        if df.loc[i]['exchange'] == exchange:
            apikey = df.loc[i,'apikey']
            secret = df.loc[i,'secret']
    exec('exchange = ccxt.' + exchange + "({'apikey':" + apikey + "'secret':" + secret + "})" )
    if exchange.has['fetchOpenOrders']:
        exchange.options["warnOnFetchOpenOrdersWithoutSymbol"] = False
        openOders = []
        orders = exchange.fetchOpenOrders()
        for openOrder in orders:
            openOders.append([openOrder['id'], openOrder['symbol'], openOrder['side'], openOrder['price'], openOrder['amount']])
        return openOders#liste de liste [id, symbol, SELL/BUY, price, amount]

#Cancel order:
def cancelOrder(exchange: str, orderId, symbol: str): #ex: cancelOrder(binance, 11480381, 'MFT/BTC')
    apikey = APIkeys_fetching()
    df = apikey.get()
    for i, row in df.iterrows():
        if df.loc[i]['exchange'] == exchange:
            apikey = df.loc[i,'apikey']
            secret = df.loc[i,'secret']
    exec('exchange = ccxt.' + exchange + "({'apikey':" + apikey + "'secret':" + secret + "})" )
    try:
        exchange.cancelOrder(orderId, symbol)
        return str('Order canceled')
      except: #if there is an error
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Responsemessage = QtWidgets.QDialog()
        ui = errorMessage.Ui_Responsemessage()
        errorMessage.ui.setupUi(Responsemessage)
        Responsemessage.show()
        sys.exit(app.exec_())

      #(ex: cancelOrder(binance, 11480381, 'MFT/BTC'))
  
#créer un ordre
def createOrder(exchange: str, symbol: str, amount: float, price: float, side: str, type: str):# (side= 'buy' or 'sell'), type = 'limit' or 'market'
    #binance.create_order('RVN/BTC', 'limit', 'buy', amount = 1.0, price = 0.060154)
    apikey = APIkeys_fetching()
    df = apikey.get()
    for i, row in df.iterrows():
        if df.loc[i]['exchange'] == exchange:
            apikey = df.loc[i,'apikey']
            secret = df.loc[i,'secret']
    exec('exchange = ccxt.' + exchange + "({'apikey':" + apikey + "'secret':" + secret + "})" )
    try:
        order = exchange.create_order(symbol, type, side, amount, price)
    except:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Responsemessage = QtWidgets.QDialog()
        ui = errorMessage.Ui_Responsemessage()
        errorMessage.ui.setupUi(Responsemessage)
        Responsemessage.show()
        sys.exit(app.exec_())
    return order
