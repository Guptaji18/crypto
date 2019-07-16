
def decryptTansposition(text):
   splittedtext=text.split(" ")
   #print(splittedtext)
   decryptedtext=''
   for splittxt in splittedtext:
      #print(splittxt[::-1])
      decryptedtext = decryptedtext + splittxt[::-1] +" "
   return(decryptedtext)