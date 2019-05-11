class addresses():
    def __init__(self):
        self.addressesInfo = pd.DataFrame(columns=['id', 'address', 'symbol'])
        if os.path.isfile('addresseInfo.csv'):
            with open('addresseInfo.csv', 'r') as f:
                self.addressesInfo = pd.read_csv(f)
        else:
            f = open('addresseInfo.csv', 'a')
            f.close()
            self.addressesInfo = pd.DataFrame(
                columns=['id', 'address', 'symbol'])
            self.addressesInfo.to_csv('addresseInfo.csv')

    def add(self, Id, address, symbol):
        self.addressesInfo.append([Id, address, symbol])
        self.addressesInfo.to_csv('addresseInfo.csv')
        
    def addressesList(self):
        liste = []
        for i, row in self.addressesInfo.iterrows():
            liste2=[]
            for info in row:
                liste2.append([info])
            liste.append(liste2)
        return liste
