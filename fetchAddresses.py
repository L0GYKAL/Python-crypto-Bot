# management des adresses


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
