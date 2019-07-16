def TranspositionCipher(text):
   splittedtext=text.split(" ")
   #print(splittedtext)
   encryptedtext=''
   for splittxt in splittedtext:
      #print(splittxt[::-1])
      encryptedtext = encryptedtext + splittxt[::-1] +" "
   return(encryptedtext)

