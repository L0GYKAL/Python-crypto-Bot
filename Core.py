import APIkeys_fetching.py
import tutorial.py
import FirstBoot.py
import pandas as pd
import ccxt
import sys


def boot():
    global MDP, exchangesDict, exchangesDf
    # MDP  =  lancer l'interface graphique, si c'est la première fois qu'il lance le programme -> MDP
    APIobject = APIKeys()
    if APIobject.firstTime() == True:
        firstboot()
    else:
        APIobject.run(MDP)
    exchangesDict = APIobject.get()
    exchangesDf = pandas.DataFrame( columns=['id','type', 'apiKey', 'secret'])
    openExchanges()


def openExchanges():
    global exchangesDf
    exchangeSerie = pd.Series(dtype=ccxt)
    for i in exchangesDf.index:
        code = 'exchangeSerie.set_value(' + i + ',' + exchangesDf.index[i] + "ccxt." + exchangesDf.Type[i] + \
            "({" + exchangesDf.PublicKey[i] + \
            ',' + exchangesDf.PrivateKey[i] + '}))'
        exec(code)
    exchangesDf.append(exchangeSerie)


if __name__ == '__main__':
    if not sys.version >= '3.6':
        print('This script requires Python 3.6+')
        sys.exit()
    else:
    boot()
