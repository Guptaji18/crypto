#!/usr/bin/env python3
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
        print('if print')
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
def vigenere(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 
       
'''
string = input("Enter the text : ")
keyword = input("Enter the keyword : ")
key = generateKey(string, keyword) 
cipher_text = vigenere(string,key) 
print("Ciphertext :", cipher_text) '''
