
#!/usr/bin/env python3
def d_ceaserDecrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
'''  
#check the above function 
text = input("Enter the text : ")
s = int(input("Enter the Shift : "))
#print "Text  : " + text 
#print "Shift : " + str(s) 
print ("Cipher: " + ceaserEncrypt(text,s)) '''