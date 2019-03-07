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

def balances(Exchanges_balances: list) -> int: #changer le nom de la variable, liste de dictionnaires avec les soldes de chaque compte en différentes crypto
    for balance in Exchanges_balances:
        for crypto in balance:
            TotalBTC=amount*priceInBTC
            TotalUSD=amount*priceInUSD
            TotalEUR=amount*priceInEUR
    
    


def main():
  knownExchanges=Exchanges()
  knownExchanges.openExchanges()
  for exchange in exchanges:
    exchange.fetchBalance()
    exchange.fetchMyTrades()
   

