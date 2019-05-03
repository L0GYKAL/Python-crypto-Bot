import APIkeys_fetching.py
import tutorial.py
import GUI\\LoginRegistration.py
import pandas as pd
import ccxt
import sys


def boot():
    global MDP, exchangesDf
    
    APIobject = APIKeys()
    if APIobject.firstTime() == True:#c'est la première fois que ça a été lancé
        register_user()# MDP  =  lancer l'interface graphique, si c'est la première fois qu'il lance le programme -> MDP
        APIobject.run(MDP)
    else:
        login()
        APIobject.run(MDP)
    #openExchanges()


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
