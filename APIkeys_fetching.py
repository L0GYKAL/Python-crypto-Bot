from Crypto.Cipher import AES, ARC2, ARC4  # pip install pycrypto
import hashlib # pip install hashlib
import base64  # pip install base64
import json
import os


class APIkeys:

    def __init__(self, Pass):
        self.exchanges = []
        self.decrypt_dictionnary = ''
        self.Pass = Pass
        self.fileName = 'APIkeys.json'
        with open('Checksum.txt', 'r') as f:
            self.Checksum=f.readline()
        self.decrypt_APIKeys()

    def run(self, Pass):#methode used to decrypt the keys with a password
        if self.checksum():
            self.decrypt_APIKeys()
        else:
            print ('Wrong Password')
        

    def fetch_APIkeys(self):
        if os.path.isfile(self.fileName):
            with open(self.fileName, 'r') as f:
                line_file = ''
                for line in f:
                    line_file = line_file + line
                return line_file
        else:
            myfile = open(self.fileName, 'a')
            myfile.close()
            return self.cypher_aes(self.Pass, '{}', encrypt=True)

    def write_APIkeys(self):
        with open(self.fileName, 'w') as f:
            crypt_dictionnary = self.cypher_aes(
                self.Pass, self.decrypt_dictionnary, encrypt=True)
            f.writelines(crypt_dictionnary)

    def cypher_aes(secret_key, msg_text, encrypt=True):
        # an AES key must be either 16, 24, or 32 bytes long
        # in this case we make sure the key is 32 bytes long by adding padding and/or slicing if necessary
        remainder = len(secret_key) % 16
        modified_key = secret_key.ljust(
            len(secret_key) + (16 - remainder))[:32]

        # input strings must be a multiple of 16 in length
        # we achieve this by adding padding if necessary
        remainder = len(msg_text) % 16
        modified_text = msg_text.ljust(len(msg_text) + (16 - remainder))

        # use of ECB mode in enterprise environments is very much frowned upon
        cipher = AES.new(modified_key, AES.MODE_ECB)
        ARC2obj=ARC2.new(modified_key + modified_key )
		ARC4obj=ARC4.new(modified_key + modified_key + modified_key)

        if encrypt:
            return base64.b64encode(ARC4obj.encrypt(ARC2obj.encrypt(AESobj.encrypt(modified_text)))).strip()

        return AESobj.decrypt(ARC2obj.decrypt(ARC4obj.decrypt(base64.b64decode(modified_text)))).strip()

    # MANAGE apikeys
    # les paramètres sont des strings

    def add_APIkeys(self, exchangeName, exchange, publicKey, secretKey):
        """Permet de vérifier si l'exchange existe déjà ou pas
        et ajouter l'exchange au dictionnaire puis l'écrire dans le dictionnaire crypté"""
        if self.exchangeExist(exchangeName, exchange, publicKey, secretKey):
            print('This exchange already exist. Try to edit it')
        else:
            self.decrypt_dictionnary[exchangeName] = [
                exchange, publicKey, secretKey]
            self.write_APIkeys()

    def edit_APIKeys(self, exchangeName, exchange, publicKey, secretKey):
        """Permet de vérifier si l'exchange existe déjà ou pas
        et éditer l'exchange sur le dictionnaire puis l'écrire dans le dictionnaire crypté"""
        if self.exchangeExist(exchangeName, exchange, publicKey, secretKey):
            self.decrypt_dictionnary[exchangeName] = [
                exchange, publicKey, secretKey]
            self.write_APIkeys()
        else:
            print("This exchange doesn't exist!")

    def del_APIkeys(self, exchangeName):
        if self.exchangeExist(exchangeName):
            del self.decrypt_dictionnary[exchangeName]
        else:
            print('There is no exchange named: ' + exchangeName)
        self.write_APIkeys()

    def decrypt_APIKeys(self):
        self.decrypt_dictionnary = json.dumps(self.cypher_aes(
            self.MDP, self.fetch_APIkeys(self), encrypt=False))

    def exchangeExist(self, exchangeName='', exchange='', publicKey='', secretKey=''):
        """regarde si l'exchange existe déjà, en regardant si les nom donné par l'utilisateur
        existe déjà et si le couple clé privée et clé publique existe déjà"""
        for exchangeNames, data in self.decrypt_dictionnary.items():
            if ((exchangeNames == exchangeName) or (data[2] == secretKey and data[1] == publicKey and data[0] == exchange)):
                return True
        return False

    def get(self):  # la methode get à été créée pour garder l'encapsulation dans la programmation orientée objet
        return self.decrypt_dictionnary
    
    def checksum(self):
        if self.Checksum == '':
            return True
        elif hashlib.sha224(self.Pass).hexdigest() == self.Checksum:
            return True
        else:
            return False
            
