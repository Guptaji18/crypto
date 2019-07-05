#!/usr/bin/env python3

from cipher.ceaser import *
from cipher.vigenere import *
from cipher.atbash import *
from cipher.railfence import *

while True:
	print('1. Ceaser Cipher')
	print('2. Vigenere Cipher')
	print('3. Atbash Cipher')
	print('4. Rail-Fence Cipher')
	print('6. Exit')
	choose = input('\n\nChoose the Cipher to encrypt the text : ')
	
	if choose == '1':
		print('\n\n***********************Ceaser Cipher***********************\n\n')
		text = input("Enter the text : ")
		s = int(input("Enter the Shift : "))
		print ("\nCipher text: " + ceaserEncrypt(text,s) + '\n\n')

	elif choose == '2':
		print('\n\n***********************Vigenere Cipher***********************\n\n')
		text = input("Enter the text : ")
		keyword = input("Enter the keyword : ")
		key = generateKey(text, keyword) 
		cipher_text = vigenere(text,key) 
		print("\nCipher text : " + cipher_text + '\n\n')
	
	elif choose == '3':
		print('\n\n***********************Atbash Cipher***********************\n\n')
		message = input('Enter the text : ')
		print('\nCipher text : ' + (atbash(message.upper())) + '\n\n')
	
	elif choose == '4':
		print('\n\n***********************Rail-Fence Cipher***********************\n\n')
		text = input('Enter the string : ')
		key = int(input('Enter the Key : '))
		print('\nCipher text : ' + encryptRailFence(text , key) + '\n\n')
	
	elif choose == '6' :
		exit()
	else :
		print('\n\n******************Invalid Input******************\n\n')
