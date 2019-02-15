from Crypto.Cipher import AES  # pip install pycrypto
import base64 # pip install base64
import getpass # pip install getpass
import json
import os

class APIkeys:

    def __init__(self):
        self.exchanges=[]
        self.decrypt_dictionnary = ''
        self.Pass = ''
        self.fileName='APIkeys.json'
        self.fetch_APIkeys()
    def fetch_APIkeys(self):
        if os.path.isfile(self.fileName):
            with open(self.fileName, 'r') as f:
                line_file=''
                for line in f:
                    line_file = line_file + line
                return line_file
        else:
            myfile = open(self.fileName, 'a')
            myfile.close()
            return cypher_aes(self.Pass, '{}', encrypt=True)
    def write_APIkeys(self):
        with open(self.fileName, 'w') as f:
            crypt_dictionnary = self.cypher_aes(self.Pass, self.decrypt_dictionnary, encrypt=True)
            f.writelines(crypt_dictionnary)
    def askPassword(self):
        self.Pass = getpass.getpass(prompt='Password:')
    def cypher_aes(secret_key, msg_text, encrypt=True):
        # an AES key must be either 16, 24, or 32 bytes long
        # in this case we make sure the key is 32 bytes long by adding padding and/or slicing if necessary
        remainder = len(secret_key) % 16
        modified_key = secret_key.ljust(len(secret_key) + (16 - remainder))[:32]

        # input strings must be a multiple of 16 in length
        # we achieve this by adding padding if necessary
        remainder = len(msg_text) % 16
        modified_text = msg_text.ljust(len(msg_text) + (16 - remainder))

        # use of ECB mode in enterprise environments is very much frowned upon
        cipher = AES.new(modified_key, AES.MODE_ECB)

        if encrypt:
            return base64.b64encode(cipher.encrypt(modified_text)).strip()

        return cipher.decrypt(base64.b64decode(modified_text)).strip()


    # MANAGE apikeys
    # les paramètres sont des strings
    def add_APIkeys(self, exchangeName, exchange, publicKey, secretKey):
        """Permet de vérifier si l'exchange existe déjà ou pas
        et ajouter l'exchange au dictionnaire puis l'écrire dans le dictionnaire crypté"""
        if self.exchangeExist(exchangeName, exchange, publicKey, secretKey):
            print('This exchange already exist. Try to edit it')
        else:
            self.decrypt_dictionnary[exchangeName] = [exchange, publicKey, secretKey]
            self.write_APIkeys()

    def edit_APIKeys(self, exchangeName, exchange, publicKey, secretKey):
        """Permet de vérifier si l'exchange existe déjà ou pas
        et éditer l'exchange sur le dictionnaire puis l'écrire dans le dictionnaire crypté"""
        if self.exchangeExist(exchangeName, exchange, publicKey, secretKey):
            self.decrypt_dictionnary[exchangeName] = [exchange, publicKey, secretKey]
            self.write_APIkeys()
        else:
            print("This exchange doesn't exist!")

    def del_APIkeys(self,exchangeName):
        if self.exchangeExist(exchangeName):
            del self.decrypt_dictionnary[exchangeName]
        else:
            print('There is no exchange named: ' + exchangeName)
        write_APIkeys(self.decrypt_dictionnary)

    def decrypt_APIKeys(self):
        self.askPassword()
        self.decrypt_dictionnary = json.dumps(self.cypher_aes(
            self.MDP, self.fetch_APIkeys(self.fileName), encrypt=False))


    def exchangeExist(self, exchangeName='', exchange='', publicKey='', secretKey=''):
        """regarde si l'exchange existe déjà, en regardant si les nom donné par l'utilisateur
        existe déjà et si le couple clé privée et clé publique existe déjà"""
        for exchangeNames, data in self.decrypt_dictionnary.items():
            if ((exchangeNames == exchangeName) or (data[2] == secretKey and data[1] == publicKey and data[0] == exchange)):
                return True
        return False
