import APIkeys_fetching.py
import tutorial.py
import FirstBoot.py
import pandas as pd
import ccxt


def boot():
    global MDP, exchangesDict, exchangesDf
    # MDP  =  lancer l'interface graphique, si c'est la première fois qu'il lance le programme -> MDP
    if firstTime == True:
        firstboot()
    APIobject = APIKeys()
    APIobject.run(MDP)
    exchangesDict = APIobject.get()
    exchangesDf = pandas.DataFrame.from_dict(exchangesDict, orient='index', columns=[
                                             'Type', 'PublicKey', 'PrivateKey'])
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
    boot()
    
    
    
#deuxième version
import APIkeys_fetching.py
import tutorial.py
import FirstBoot.py
import pandas as pd
import ccxt


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
    boot()
