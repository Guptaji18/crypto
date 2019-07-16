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
    while i < len(user_input):
        for key in table:
            if user_input[i:i+2] == table.get(key):
                decrypt += key
        i += 2
    print("     Original message: " + user_input)
    print("     Decrypted message: " + decrypt)
    i = 0
    decrypt = ""
    
