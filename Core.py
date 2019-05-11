import APIkeys_fetching.py
import tutorial.py
import GUI.mainscreen3final.py
import pandas as pd
import ccxt
import sys


def boot():
    global MDP, exchangesDf

    if is_connected():
        APIobject = APIKeys()
        if APIobject.firstTime() == True:  # c'est la première fois que ça a été lancé
            register_user()  # MDP  =  lancer l'interface graphique, si c'est la première fois qu'il lance le programme -> MDP
            APIobject.run(MDP)
        else:
            login()
            while (APIobject.password(MDP)) != True:
                login()
                APIobject.password(MDP)
            APIobject.run(MDP)
    else:
        print('No internet!')
        sys.exit()

if __name__ == '__main__':
    if not sys.version >= '3.6':
        print('This script requires Python 3.6+')
        sys.exit()
    else:
        boot()
