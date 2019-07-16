import string

global table
table = {}
# List of valid character input
global reference_table
reference_table = list(string.printable)

def enigma(user_input):
    encrypt = ""  # String used for encryption
    i = j = 0     # increment variables
    k = 0

    # reference_table is mapped to integer values
    for j in reference_table:
        # map a casted integer to a table value
        table[j] = str(k).zfill(2)
        k += 1
    for c in user_input:
        for key in table:
            if c == key:
                # add each matching character one at a time to
                # the encrypted message
                encrypt += table.get(key)
    return encrypt
    #print("Original message: " + user_input)
    #print("Encrypted message: " + encrypt)
    i = 0
    encrypt = ""
    
enigma(hello)