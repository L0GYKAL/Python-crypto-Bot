#-------------------------------------------------------------------------------
# Name:    	module1
# Purpose:
#
# Author:  	antoine.mouran
#
# Created: 	25/01/2019
# Copyright:   (c) antoine.mouran 2019
# Licence: 	<your licence>
#-------------------------------------------------------------------------------

import json
import pickle


def write_APIkeys(keys, filename="APIkeys.json"):
	with open(filename, 'w') as f:
    	pickle.dump(keys, f)

def fetch_APIkeys(filename="APIkeys.json"):
	with open(filename, 'r') as f:
        	return dict(json.load(f))

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

def askPassword():
	MDP=input('Mot de passe:')
	return MDP

def passwordForm():
	MDP = askPassword()
	len=len(MDP)
	while len != 16:
    	MDP=list(MDP)
    	MDP.append('*')
    	len=len(MDP)
	MDP=str(MDP)





#chiffrement: PS: message est le fichier
####importation des librairies:
import Crypto,hashlib,os,sys,string,gtk
from Crypto.Cipher import AES
from Crypto.Cipher import ARC2
from Crypto.Cipher import ARC4

#https://codes-sources.commentcamarche.net/source/52273-crypte-et-decrypte-un-fichier-avec-hash-pour-verification
#https://docs.python-guide.org/scenarios/crypto/

####adaptation de la longeur du message pour qu il soit multiple de 16 (plus ajout du hash)
def   adaptline(line,div):
	pre_chk=checksum(line)
	lena=len(line+pre_chk)
	addnb=((((lena/div)+1)*div)-lena)
	if addnb>0 and addnb<10: addnb=addnb+div
	lenad=len(str(addnb))
	nline= str(addnb) + ((addnb-lenad) * " ") + line + pre_chk
	return nline

####suppression des caracteres ajoutés lors de l'adaptation (plus verification du hash)
def  realeaseline(line):
	n=line[0:2:1]
	new=line[int(n):int(len(line)):1]
	message=new[0:len(new)-56:1]
	chk=new[len(new)-56::1]
	if checksum(message)==chk:
    	return message

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
