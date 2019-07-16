#!/usr/bin/env python3


print('\n\n#################################################')
print('******MADE BY : SHIKHAR GUPTA******')
print('********** TEXT ENCRYPTOR OR DECRYPTOR ***********')

print('#################################################\n\n')

import string
from cipher.rot13 import *
from cipher.vigenere import *
from cipher.atbash import *
from cipher.railfence import *
from cipher.Affine import *
from cipher.Transposing import *
from cipher.bff import *
from d_cipher.d_rot13 import *
from d_cipher.d_vigenere import *
from d_cipher.d_atbash import *
from d_cipher.d_railfence import *
from d_cipher.d_Affine import *
from d_cipher.d_transposition import *

global table
table = {}
# List of valid character input
global reference_table
reference_table = list(string.printable)
encrypt = ""  
decrypt = ""
i = j = 0     # increment variables
k = 0

# reference_table is mapped to integer values
for j in reference_table:
    # map a casted integer to a table value
    table[j] = str(k).zfill(2)
    k += 1

while True:
	#print('What you Want to perform Encryption (e) or Decryption (d) ? ')
	choise = input('\nWhat you Want to perform Encryption (e) or Decryption (d) or Quit (q)? ')
	if choise == 'e' or choise == 'E':
		print('\n\n#################################################')

		print('********** ENCRYPTION ***********')

		print('#################################################\n\n')
		while True:
			print('1. ROT 13')
			print('2. Vigenere Cipher')
			print('3. Atbash Cipher')
			print('4. Rail-Fence Cipher')
			print('5. Affine Cipher')
			print('6. Transposition Cipher')
			print('7. Enigma')
			print('8. Brainf**k')
			print('9. Exit')
			choose = input('\n\nChoose the Cipher to encrypt the text : ')
			
			if choose == '1':
				print('\n\n***********************ROT 13***********************\n\n')
				text = input("Enter the text : ")
				#s = int(input("Enter the Shift : "))
				print ("\nCipher text: " + ceaserEncrypt(text,13) + '\n\n')
				break

			elif choose == '2':
				print('\n\n***********************Vigenere Cipher***********************\n\n')
				text = input("Enter the text : ")
				text = text.upper()
				keyword = input("Enter the keyword : ")
				keyword = keyword.upper()
				key = generateKey(text, keyword) 
				cipher_text = vigenere(text,key) 
				print("\nCipher text : " + cipher_text + '\n\n')
				break
			
			elif choose == '3':
				print('\n\n***********************Atbash Cipher***********************\n\n')
				message = input('Enter the text : ')
				print('\nCipher text : ' + (atbash(message.upper())) + '\n\n')
				break
			
			elif choose == '4':
				print('\n\n***********************Rail-Fence Cipher***********************\n\n')
				text = input('Enter the string : ')
				key = int(input('Enter the Key : '))
				print('\nCipher text : ' + encryptRailFence(text , key) + '\n\n')
				break

			elif choose == '5':
				print('\n\n***********************Affine Cipher***********************\n\n')
				text=str(input('Enter the String: '))
				key = [17, 20]
				affine_encrypted_text = affine_encrypt(text, key) 
				print('\nCipher Text: {}'.format( affine_encrypted_text ) + '\n\n')
				break
				

			elif choose == '6':
				print('\n\n***********************Transposition Cipher***********************\n\n')
				text = input("Enter the String : ")
				print('\nCipher text : ' + TranspositionCipher(text) + '\n\n'  )
				break

			elif choose == '7':
				print('\n\n***********************Enigma***********************\n\n')
				user_input = input("Enter the text : ")
				for c in user_input:
					for key in table:
						if c == key:
							encrypt += table.get(key)
				print('\nCipher text : ' + encrypt + '\n\n'  )
				i = 0
				encrypt = ""

				break

			elif choose == '8':
				print('\n\n***********************Brainf**k Cipher***********************\n\n')
				text = input("Enter the String : ")
				result = str2bf(text)
				result = result.replace(" ", "").replace("\n", "")
				print ('\nCipher text : ' + result + '\n\n' )
				break

			elif choose == '9' :
				exit()
			else :
				print('\n\n******************Invalid Input******************\n\n')

	elif choise == 'd' or choise =='D':
		print('\n\n#################################################')

		print('********** DECRYPTION ***********')

		print('#################################################\n\n')
		while True:

			print('1. ROT 13')
			print('2. Vigenere Cipher')
			print('3. Atbash Cipher')
			print('4. Rail-Fence Cipher')
			print('5. Affine Cipher')
			print('6. Transposition Cipher')
			print('7. Enigma')
			#print('8. Brainf**k')
			print('9. Exit')
			choose = input('\n\nChoose the Cipher to Decrypt the text : ')
			
			if choose == '1':
				print('\n\n***********************ROT 13***********************\n\n')
				text = input("Enter the Ciphertext : ")
				#s = int(input("Enter the Shift : "))
				print ("\nPlain text: " + d_ceaserDecrypt(text,13) + '\n\n')
				break

			elif choose == '2':
				print('\n\n***********************Vigenere Cipher***********************\n\n')
				text = input("Enter the Ciphertext : ")
				text = text.upper()
				keyword = input("Enter the keyword : ")
				keyword = keyword.upper()
				key = generateKey(text, keyword) 
				cipher_text = d_vigenere(text,key) 
				print("\nPlain text : " + cipher_text + '\n\n')
				break
			
			elif choose == '3':
				print('\n\n***********************Atbash Cipher***********************\n\n')
				message = input('Enter the Ciphertext : ')
				print('\nPlain text : ' + (d_atbash(message.upper())) + '\n\n')
				break
			
			elif choose == '4':
				print('\n\n***********************Rail-Fence Cipher***********************\n\n')
				text = input('Enter the Ciphertext : ')
				key = int(input('Enter the Key : '))
				print('\nPlain text : ' + decryptRailFence(text , key) + '\n\n')
				break

			elif choose == '5':
				print('\n\n***********************Affine Cipher***********************\n\n')
				text=str(input('Enter the Ciphertext : '))
				key = [17, 20] 
				print('\nDecrypted Text: {}'.format
				( affine_decrypt(text, key) )+ '\n\n' ) 
				break
				

			elif choose == '6':
				print('\n\n***********************Transposition Cipher***********************\n\n')
				text = input("Enter the Ciphertext : ")
				print('\nPlain text : ' + decryptTansposition(text) + '\n\n'  )
				break

			elif choose == '7':
				print('\n\n***********************Enigma***********************\n\n')
				user_input = (input("Enter the Ciphertext : "))
				while i < len(user_input):
					for key in table:
						if user_input[i:i+2] == table.get(key):
							decrypt += key
					i += 2
				print('\nPlain text : ' + decrypt + '\n\n'  )
				i = 0
				encrypt = ""
				break

			elif choose == '8':
				print("Try another option")

			elif choose == '9' :
				exit()
			else :
				print('\n\n******************Invalid Input******************\n\n')
	elif choise == 'q' or choise == 'Q':
		exit()
		
		
	else :
			print('\n\n******************Invalid Input******************\n\n')



