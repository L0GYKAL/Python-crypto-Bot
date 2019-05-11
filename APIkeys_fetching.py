import pandas as pd
import os

class APIkeys():
    def __init__(self):
        self.fileName = 'exchangeCSV.csv'
        self.exchangesInfo = pd.DataFrame(
                index = ['upbit', 'kucoin', 'kraken', 'coss', 'bittrex', 'bitfinex', 'binance'],
                {'exchange':['upbit', 'kucoin', 'kraken', 'coss', 'bittrex', 'bitfinex', 'binance'], 'id': [], 'apikey': [], 'secret': []}
                )
        if self.firstTime():
            write(elf.exchangesInfo)
        self.exchangesInfo = self.read()


    def firstTime(self) -> bool: #vérifie si c'est la première connection
        if os.path.isfile(self.fileName):
            return False
        else:
            return True

    def read(self): #lecture du fichier
        with open(self.fileName, 'r') as f:
            exchangeCSV = pd.read_csv(f)    #voir si je fais un chiffrement
            return exchangeCSV

    def write(exchangesInfo: Df): #écriture dans le fichier
        pd.DataFrame.to_csv(self.fileName)
        
    def get(self):
        return self.exchangeInfo

    #management des clés API

    def editKeys(self, exchange: str, Id: str, apiKey: str, secret: str):
        self.exchangesInfo.loc[exchange] = [exchange] + [Id] + [apikey] + [secret]
        write(self.exchangesInfo)
