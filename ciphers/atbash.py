#!/usr/bin/env python3

lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'} 
  
def atbash(message): 
    cipher = '' 
    for letter in message: 
        # checks for space 
        if(letter != ' '): 
            #adds the corresponding letter from the lookup_table 
            cipher += lookup_table[letter] 
        else: 
            # adds space 
            cipher += ' '
  
    return cipher 

'''    
message = input('Enter the text : ')
print('Cipher text : ' + (atbash(message.upper())))'''

