import APIkeys_fetching.py
import ccxt

exchanges=[]
def openExchanges():
  global exchanges
  for exchange, data in decrypt_dictionnary.items():
    exec(“exchanges.append(%s = %d.%e(%f,%g))” %(data[0], 'ccxt', data[0], data[1], data[2]))



def main():
  openExchanges()
  for exchange in exchanges:
    exchange.fetchBalance
    exchange.fetchMyTrades
