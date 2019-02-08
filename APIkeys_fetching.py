from Crypto.Cipher import AES  # pip install pycrypto
import base64
import getpass
import json

decrypt_dictionnary=''
MDP=''

def fetch_APIkeys(filename="APIkeys.json"):
    global decrypt_dictionnary
    with open(filename, 'r') as f:
        for line in f:
        line_file= line_file + line
        return line_file






def askPassword():
    global MDP
	MDP=getpass.getpass(prompt='Password:')

def cypher_aes(secret_key, msg_text, encrypt=True):
    # an AES key must be either 16, 24, or 32 bytes long
    # in this case we make sure the key is 32 bytes long by adding padding and/or slicing if necessary
    remainder = len(secret_key) % 16
    modified_key = secret_key.ljust(len(secret_key) + (16 - remainder))[:32]
    print(modified_key)

    # input strings must be a multiple of 16 in length
    # we achieve this by adding padding if necessary
    remainder = len(msg_text) % 16
    modified_text = msg_text.ljust(len(msg_text) + (16 - remainder))
    print(modified_text)

    cipher = AES.new(modified_key, AES.MODE_ECB)  # use of ECB mode in enterprise environments is very much frowned upon

    if encrypt:
        return base64.b64encode(cipher.encrypt(modified_text)).strip()

    return cipher.decrypt(base64.b64decode(modified_text)).strip()



def main():
    askPassword()
    decrypt_dictionnary=cypher_aes(MDP, fetch_APIkeys(filename="APIkeys.json"), encrypt=True)
    APIkeys=json.dumps(decrypt_dictionnary)
