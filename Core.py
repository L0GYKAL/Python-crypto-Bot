import APIkeys_fetching.py
import ccxt

class Exchanges:
    def __init__(self):
        self.exchangesList=[]
        self.APIobject=APIKeys()
        #demande le mot de passe
        self.APIobject.run('Mot de Passe')
        self.dictionnary=self.APIobject.get()

    def openExchanges(self):
      for exchange, data in self.dictionnary.items():
        exec(“self.exchangesList.append(%s = %d.%e(%f,%g))” %(data[0], 'ccxt', data[0], data[1], data[2]))



def main():
  openExchanges()
  for exchange in exchanges:
    exchange.fetchBalance
    exchange.fetchMyTrades
