def convert(Amount: int, Token: str) -> int: #amount in BTC
  priceInBTC=Amount*price
  
  https://stackoverflow.com/questions/9195455/how-to-document-a-method-with-parameters
    
    def balances(exchanges: Exchanges):
    balances=[]
    for exchange in exchanges.exchangesList:
        balances.append(exchanges.exchangesList[i].fetchBalance())




  
  #THIS WORKS
import ccxt
import pandas as pd
total = float()
binance = ccxt.binance({
   'id':
   'Binance',
   'apiKey':
   '',
   'secret':
   ''
})
balances = binance.fetchBalance()
# print(balances)
balances = pd.DataFrame(data=balances['info']['balances'])
# print(balances)
for i in balances.index:
   if balances.loc[i, 'asset'] == 'BTC':
       balInBTC = float(balances.loc[i, 'free']) + float(
           balances.loc[i, 'locked'])
       print('You have ' + str(
           float(balances.loc[i, 'free']) + float(balances.loc[i, 'locked'])
       ) + ' ' + balances.loc[i, 'asset'] + ' It represents ' + str(balInBTC))
       total += balInBTC
   elif balances.loc[i, 'asset'] == 'VTHO':
       pass
   elif float(balances.loc[i, 'free']) + float(
           balances.loc[i, 'locked']) != 0:
try:
       ticker = binance.fetchTicker(balances.loc[i, 'asset'] + '/BTC')
except:
     ticker['last']=0
       balInBTC = ticker['last'] * (
           float(balances.loc[i, 'free']) + float(balances.loc[i, 'locked']))
       print('You have ' + str(
           float(balances.loc[i, 'free']) + float(balances.loc[i, 'locked'])
       ) + ' ' + balances.loc[i, 'asset'] + ' It represents ' + str(balInBTC))
       total += balInBTC
print('You have an aproximated amount of BTC: '+ total)
#reste a vérifier si la paires existe dans le market  avec loadMarkets()
