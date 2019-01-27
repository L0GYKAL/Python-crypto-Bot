#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      antoine.mouran
#
# Created:     25/01/2019
# Copyright:   (c) antoine.mouran 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import json


def write_APIkeys(keys, filename="APIkeys.json"):
    with open(filename, 'w') as f:
        json.dump(keys, f)

def fetch_APIkeys(filename="APIkeys.json"):
    with open(filename, 'r') as f:
            return json.load(f)

def add_APIkeys(exchangeName, exchange, publicKey, secretKey, filename="APIkeys.json"): # les paramètres sont des strings
    keys=fetch_APIkeys()
    if exchangeName not in keys:
        keys[exchangeName]=[exchange,publicKey, secretKey]
    else:
        print('This exchange  exist.')
    write_APIkeys(keys)

def del_APIkeys(exchangeName, filename="APIkeys.json"):
    keys=fetch_APIkeys()
    try:
        del keys[exchangeName]
    except KeyError:
        print('There is no exchange named: '+ exchangeName)
        write_APIkeys(keys)

#chiffrement: PS: message est le fichier
####importation des librairies:
import Crypto,hashlib,os,sys,string,gtk
from Crypto.Cipher import AES
from Crypto.Cipher import ARC2
from Crypto.Cipher import ARC4

#https://codes-sources.commentcamarche.net/source/52273-crypte-et-decrypte-un-fichier-avec-hash-pour-verification


#transformer pour avoir un fichier dictionnaire sans avoir de fichier décrypté
####fonction de cryptage pour un fichier
def cryptfile(original_filename, Key , destination_filename):
	line_file= ""
	FILE_O = open(original_filename,"r")
	FILE_D = open(destination_filename,"w")
	for line in FILE_O:
		line_file= line_file + line
	line_file=adaptline(line_file,16)
	crypt_line=crypt(line_file,Key)
	FILE_D.writelines(crypt_line)

	FILE_O.close()
	FILE_D.close()

#fonctionde decryptage pour un fichier
def decryptfile(original_filename, Key, destination_filename):
	line_file= ""
	FILE_O = open(original_filename,"r")
	FILE_D = open(destination_filename,"w")
	for line in FILE_O:
		line_file= line_file + line
	crypt_line=decrypt(line_file,Key)
	crypt_line=realeaseline(crypt_line)
	FILE_D.writelines(crypt_line)
	FILE_O.close()
	FILE_D.close()
