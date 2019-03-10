from Crypto.Cipher import AES, ARC2, ARC4  # pip install pycrypto
import hashlib  # pip install hashlib
import base64  # pip install base64
import json
import os

#https://stackoverflow.com/questions/52116171/how-to-encrypt-and-decrypt-pandas-dataframe-with-decryption-key
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
#(http://www.datasciencemadesimple.com/encode-decode-column-dataframe-python/)


class APIkeys:

    def __init__(self, Pass):
        self.exchanges = []
        self.decrypt_dictionnary = ''
        self.Pass = Pass
        self.fileName = 'APIkeys.json'
        self.Checksum = ''

    def run(self, Pass):  # methode used to decrypt the keys with a password, Password should never be void
        self.Pass = Pass
        self.read()


def read(self):
    if os.path.isfile(self.fileName):
        with open(self.fileName, 'r') as f:
            lines = f.readlines()
        self.decrypt(lines[0], lines[1])
    else:
        myfile = open(self.fileName, 'a')
        myfile.close()
        self.decrypt('', '')


def decrypt(self, crypt_dictionnary, crypt_checksum):
    if (crypt_dictionnary != '' and crypt_checksum != ''):
        if hashlib.sha224(self.Pass).hexdigest() == self.cypher_aes(self.Pass, crypt_checksum.strip('\n'), encrypt=False):  # Good password
            self.decrypt_dictionnary = json.dumps(self.cypher_aes(
                self.Pass, crypt_dictionnary.strip('\n'), encrypt=False))
            self.checksum = hashlib.sha224(self.Pass).hexdigest()
        else:
            print('Wrong Password')
    else:
        self.decrypt_dictionnary = {}

    def write_APIkeys(self):
        crypt_lines = []
        with open(self.fileName, 'w') as f:
            crypt_lines[0] = self.cypher_aes(
                self.Pass, self.decrypt_dictionnary, encrypt=True)
            crypt_lines[1] = self.cypher_aes(
                self.Pass, self.Checksum, encrypt=True)
            f.writelines(str(line) + "\n" for line in crypt_lines)

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
        AESobj = AES.new(modified_key, AES.MODE_ECB)
        ARC2obj = ARC2.new(modified_key + modified_key)
        ARC4obj = ARC4.new(modified_key + modified_key + modified_key)

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

    def exchangeExist(self, exchangeName='', exchange='', publicKey='', secretKey=''):
        """regarde si l'exchange existe déjà, en regardant si les nom donné par l'utilisateur
        existe déjà et si le couple clé privée et clé publique existe déjà"""
        for exchangeNames, data in self.decrypt_dictionnary.items():
            if ((exchangeNames == exchangeName) or (data[2] == secretKey and data[1] == publicKey and data[0] == exchange)):
                return True
        return False

    def get(self):  # la methode get à été créée pour garder l'encapsulation dans la programmation orientée objet
        return self.decrypt_dictionnary
