import APIkeys_fetching.py
import ccxt
import pandas as pd

MDP=''
exchangesList=''
""" l'interface graphique demande un MDP (AskPass(FirstTime))
    déchiffrement du dictionnaire
    stockage des info dans une pandas datastructure
    création des objets exchanges avec ccxt
    liste des exchanges -> pandas datastructure (dernière colonne)

    global MDP, exchangesList
    """
def boot():
    #lancer l'interface graphique -> MDP
    Api=APIKeys()
    ApiDict = ApiDict.get()
    exchangesList = pd.dataframe(ApiDict, index=index)







class Exchanges:
    def __init__(self):
        self.exchangesList=generateExchanges()
        self.APIobject=APIKeys()
        #demande le mot de passe
        self.APIobject.run('Mot de Passe')
        self.dictionnary=self.APIobject.get()


    def generateExchanges(self):
      exchangesList=[]
      for exchange, data in self.dictionnary.items():
        exec(“self.exchangesList.append(%s = %d.%e(%f,%g,{'enableRateLimit': True,}))” %(data[0], 'ccxt', data[0], data[1], data[2]))
      return exchangesList

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


