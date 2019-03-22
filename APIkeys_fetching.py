from Crypto.Cipher import AES, ARC2, ARC4  # pip install pycrypto
import hashlib  # pip install hashlib
import base64  # pip install base64
import pandas as pd
import os


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_string.html

class APIkeys:
	global exchangesDf, MDP

	def __init__(self):
        self.fileName = 'APIkeys.csv'
    	self.Checksum = ''

    def run(self):  # methode used to decrypt the keys with a password, Password should never be void
            self.read()

	def cypher_aes(self,secret_key, msg_text, encrypt=True):
    	# an AES key must be either 16, 24, or 32 bytes long
    	# in this case we make sure the key is 32 bytes long by adding padding and/or slicing if necessary
    	secret_key=str(secret_key)
    	msg_text=str(msg_text)
    	remainder = len(secret_key) % 16
    	modified_key = secret_key.ljust(
        	len(secret_key) + (16 - remainder))[:32]

    	# input strings must be a multiple of 16 in length
    	# we achieve this by adding padding if necessary
    	remainder = len(str(msg_text)) % 16
    	modified_text = msg_text.ljust(len(str(msg_text)) + (16 - remainder))

    	# use of ECB mode in enterprise environments is very much frowned upon
    	AESobj = AES.new(modified_key, AES.MODE_ECB)
    	ARC2obj = ARC2.new(modified_key + modified_key)
    	ARC4obj = ARC4.new(modified_key + modified_key + modified_key)

    	if encrypt:
        	return base64.b64encode(ARC4obj.encrypt(ARC2obj.encrypt(AESobj.encrypt(modified_text)))).strip()

    	return AESobj.decrypt(ARC2obj.decrypt(ARC4obj.decrypt(base64.b64decode(modified_text)))).strip()

	def read(self):
    	global MDP, exchangesDf
    	if os.path.isfile(self.fileName):
        	with open(self.fileName, 'r') as f:
            	cryptDf = pd.read_csv(self.fileName)
    	# cypher_aes(MDP, cryptDf, encrypt=False) essayer les 2
    	#cryptDf.applymap(lambda x: self.cypher_aes(MDP, x, encrypt=False) )
            	if hashlib.sha224(MDP).hexdigest() == cryptDf.loc[0,'checksum']:
                	exchangesDf = cryptDf
    	else:
        	myfile = open(self.fileName, 'a')
        	myfile.close()
        	exchangesDf = pd.dataframe(columns=['id', 'type', 'apiKey', 'secret', 'checksum'])


	def write_APIkeys(self):
    	exchangesDf.applymap(lambda x: api.cypher_aes(MDP, x) )
    	pandas.DataFrame.to_csv(self.fileName)

    def firstTime(self) -> bool:
      if os.path.isfile(self.fileName):
          return False
      else:
          return True

    def exchangeExist(self, id: str, type: str, apiKey: str, secret: str) -> bool:
        """regarde si l'exchange existe déjà, en regardant si les nom donné par l'utilisateur
        existe déjà et si le couple clé privée et clé publique existe déjà"""

        for i in exchangesDf.index():
            if ((exchangesDf.loc[i,’id’] == id) or (exchangesDf.loc[i,’secret’] == secret and exchangesDf.loc[i,’apiKey’] == apiKey and exchangesDf.loc[i,’type’] == type)):
                return True
#management des exchanges sauvegardés
    def add_APIkeys(self, id, type, apiKey, secret):
            """Permet de vérifier si l'exchange existe déjà ou pas
            et ajouter l'exchange au dictionnaire puis l'écrire dans le dictionnaire crypté"""

            if self.exchangeExist(id, type, apiKey, secret):
                print('This exchange already exist. Try to edit it')
            else:
                exchangesDf[len(exchangesDf)] = [
                    id, type, apiKey, secret]
                self.write_APIkeys()

    def del_APIkeys(self, id):
        """Pour cette methode, il faut une liste défilante qui regarde dans exchangeDf['id']"""
        index = 0
        idList = exchangeDf['id'].tolist()
        for name in idList:
            if idList[name] == id:
                index=name
                break
        exchangesDf.drop(index)
           self.write_APIkeys()

    def edit_APIKeys(self, id, type, apiKey, secret):
        if self.exchangeExist(id, type, apiKey, secret):
        """Pour cette methode, il faut une liste défilante qui regarde dans exchangeDf['id']
            Puis la GUI affiche dans un champ de texte les info suivantes qui peuvent être modifié à sa guise:
                sauf(exchangeDf['id'] qui sera juste affiché mais pas modifiable) , exchangeDf['type'] , exchangeDf['apikey'] , exchangeDf['secret']
                Après avoir appuyé sur le boton les champs de texte se sauvegardent respectivement dans dans les variables
                type, apikey, secret """
        """Permet d'éditer l'exchange dans le dataframe puis l'écrire dans le fichier csv"""
            for i in idList:
                if idList[i] == id:
                    index=i
                    break
            exchangeDf.at[index,type]=type
            exchangeDf.at[index,apiKey]=apiKey
            exchangeDf.at[index,secret]=secret
            self.write_APIkeys()
