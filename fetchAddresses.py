# management des adresses


class addresses:
    def __init__(self):
        self.addressesInfo = pd.DataFrame(columns=['id', 'address', 'symbol'])
        if os.path.isfile('addresseInfo.csv'):
            with open('addresseInfo.csv', 'r') as f:
                self.addressesInfo = pd.read_csv(f)
        else:
            f = open('addresseInfo.csv', 'a')
            f.close()
            self.addressesInfo = pd.DataFrame(columns=['id', 'address', 'symbol'])
            self.addressesInfo.to_csv('addresseInfo.csv')
            
    def add(self, id, address, symbol):
        self.addressesInfo.append([id, address, symbol])
        self.addressesInfo.to_csv('addresseInfo.csv')
        
   class balanceHistory():
    def __init__(self):
        self.balanceHistory = pd.DataFrame(columns=['id', 'address', 'symbol'])
        if os.path.isfile('balanceHistory.csv'):
            with open('balanceHistory.csv', 'r') as f:
                self.balanceHistory = pd.read_csv(f)
        else:
            f = open('addresses.csv', 'a')
            f.close()
            balanceHistory = pd.DataFrame(columns=['id', 'address', 'symbol'])
            balanceHistory.to_csv('addresses.csv')
        
        
        
#brouillon:
"""def addressExist(id, address, symbol):
        global addressesDf
        for i in addressesDf.index():
            if ((addressesDf.loc[i, 'id'] == id) or (addressesDf.loc[i, 'address'] == address and addressesDf.loc[i, 'symbol'] == symbol)):
                return True
        return False

    def add_Address(self, id, address, symbol):
        global addressesDf
        if addressExist(id, address, symbol):
            print('This address already exist. Try to edit it')
        else:
            addressesDf.append([id, address, symbol])

    def readHistory():
        global addressesDf
        if os.path.isfile('addresses.csv'):
            with open('addresses.csv', 'r') as f:
                addressesDf = pd.read_csv(f)
        else:
            f = open('addresses.csv', 'a')
            f.close()
            balanceHistory = pd.DataFrame(columns=['id', 'address', 'symbol'])
            balanceHistory.to_csv('addresses.csv')
            
class addresses:
    def addressExist(id, address, symbol):
        global addressesDf
        for i in addressesDf.index():
            if ((addressesDf.loc[i, 'id'] == id) or (addressesDf.loc[i, 'address'] == address and addressesDf.loc[i, 'symbol'] == symbol)):
                return True
        return False

    def add_Address(self, id, address, symbol):
        global addressesDf
        if addressExist(id, address, symbol):
            print('This address already exist. Try to edit it')
        else:
            addressesDf.append([id, address, symbol])

    def readAddresses():
        global addressesDf
        if os.path.isfile('addresses.csv'):
            with open('addresses.csv', 'r') as f:
                addressesDf = pd.read_csv(f)
        else:
            f = open('addresses.csv', 'a')
            f.close()
            balanceHistory = pd.DataFrame(columns=['id', 'address', 'symbol'])
            balanceHistory.to_csv('addresses.csv')

def compileBalances():
    #
    for address in adresses:
        try:
            totalBTC += float(fetchAddress(symbol, address)) * \
                float(getPrice(symbol, 'BTC'))
        except:
            pass
    for exchange in exchanges:
        try:
            totalBTC += float(fetchExchangeBalance(exchange))
        except:
            pass
    return totalBTC


def saveBalance(totalBTC):
    row = [datetime.today(), totalBTC]
    if os.path.isfile('balanceHistory.csv'):
        with open('balanceHistory.csv', 'r') as f:
            balanceHistory = pd.read_csv(f)
        if balanceHistory.at[0, -1] != datetime.today():
            balanceHistory.append(row)
            balanceHistory.to_csv('balanceHistory.csv')
        else:
            pass
    else:
        f = open('balanceHistory.csv', 'a')
        f.close()
        balanceHistory = pd.DataFrame(columns=['date', 'BalanceInBTC'])
        balanceHistory.append(row)
        balanceHistory.to_csv('balanceHistory.csv')


def readBalances():
    if os.path.isfile('balanceHistory.csv'):
        with open('balanceHistory.csv', 'r') as f:
            balanceHistory = pd.read_csv(f)
        return balanceHistory
    else:
        f = open('balanceHistory.csv', 'a')
        f.close()
        balanceHistory = pd.DataFrame(columns=['date', 'BalanceInBTC'])
        balanceHistory.to_csv('balanceHistory.csv')"""
