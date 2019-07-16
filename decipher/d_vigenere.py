def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      

def d_vigenere(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 
      

'''
string = input("Enter text : ")
string = string.upper()
keyword = input("Enter key : ")
keyword = keyword.upper()
key = generateKey(string, keyword) 
 
print("Original/Decrypted Text :",  
    originalText(string, key)) '''
  
