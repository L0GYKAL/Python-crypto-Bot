# THIS WORKS
import ccxt
import pandas as pd


def fetchBalance(exchange):
    total = float()
# exchange[0]=ccxtObject and exchange[1]=name
    """binance = ccxt.binance({
        'id':
        'Binance',
        'apiKey':
        'QDvA3MvcZNgy0kFmsSFlBwX3VirMcV5VnhjOctTRqohH46Ces8glcRys48H8ddwX',
        'secret':
        'yISA8ODctEZY4ncjpHIxAKar638Xe9hvjmldi7TRKxQ9L1Zcb3MvSuJMDpeIG8rs'
    })"""
    balances = exchange[0].fetchBalance()
    # print(balances)
    balances = pd.DataFrame(data=balances['info']['balances'])
    exchange[0].loadMarkets()
    for i in balances.index:
        ticker = balances.loc[i, 'asset'] + '/BTC'
        if exchange[0].markets[ticker]:
            if float(balances.loc[i, 'free']) + float(
                    balances.loc[i, 'locked']) != 0:
                if balances.loc[i, 'asset'] == 'BTC':
                    balInBTC = float(balances.loc[i, 'free']) + float(
                        balances.loc[i, 'locked'])
                else:
                    balInBTC = ticker['last'] * (
                        float(balances.loc[i, 'free']) + float(balances.loc[i, 'locked']))
        print('You have ' + str(
            float(balances.loc[i, 'free']) +
            float(balances.loc[i, 'locked'])
        ) + ' ' + balances.loc[i, 'asset'] + ' It represents ' + str(balInBTC))
        total += balInBTC
    print('You have an approximate amount of' +
          total + ' BTC in ' + exchange[1])
    # reste a vérifier si la paires existe dans le market  avec loadMarkets()
