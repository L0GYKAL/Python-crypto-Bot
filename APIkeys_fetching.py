from Crypto.Cipher import AES  # pip install pycrypto
import base64
import getpass
import json

decrypt_dictionnary=''
MDP=''

def fetch_APIkeys(filename="APIkeys.json"):
    global decrypt_dictionnary
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        for line in f:
        line_file= line_file + line
        return line_file
else:
    myfile = open(filename, 'a')
    myfile.close()
	return cypher_aes(MDP, '{}', encrypt=True)

def write_APIkeys(filename="APIkeys.json"):
    with open(filename, 'w') as f:
        crypt_dictionnary=cypher_aes(MDP, decrypt_dictionnary, encrypt=True)
        f.writelines(crypt_dictionnary)





def askPassword():
    global MDP
	MDP=getpass.getpass(prompt='Password:')

def cypher_aes(secret_key, msg_text, encrypt=True):
    # an AES key must be either 16, 24, or 32 bytes long
    # in this case we make sure the key is 32 bytes long by adding padding and/or slicing if necessary
    remainder = len(secret_key) % 16
    modified_key = secret_key.ljust(len(secret_key) + (16 - remainder))[:32]

    # input strings must be a multiple of 16 in length
    # we achieve this by adding padding if necessary
    remainder = len(msg_text) % 16
    modified_text = msg_text.ljust(len(msg_text) + (16 - remainder))

    cipher = AES.new(modified_key, AES.MODE_ECB)  # use of ECB mode in enterprise environments is very much frowned upon

    if encrypt:
        return base64.b64encode(cipher.encrypt(modified_text)).strip()

    return cipher.decrypt(base64.b64decode(modified_text)).strip()


#MANAGE apikeys
def add_APIkeys(exchangeName, exchange, publicKey, secretKey, dictionnary=decrypt_dictionnary): # les paramètres sont des strings
	if exchangeName not in dictionnary:
    		dictionnary[exchangeName]=[exchange,publicKey, secretKey]
	else:
    		print('This exchange already exist.')
	write_APIkeys(dictionnary)

def del_APIkeys(exchangeName, dictionnary=decrypt_dictionnary):
	try:
    		del dictionnary[exchangeName]
	except KeyError:
    		print('There is no exchange named: '+ exchangeName)
    	write_APIkeys(dictionnary)



def decrypt_APIKeys():
    askPassword()
    decrypt_dictionnary=cypher_aes(MDP, fetch_APIkeys(filename="APIkeys.json"), encrypt=False)
    APIkeys=json.dumps(decrypt_dictionnary)
