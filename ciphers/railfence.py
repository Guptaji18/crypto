#!/usr/bin/env python3
def encryptRailFence(text, key): 
	rail = [['\n' for i in range(len(text))] 
				for j in range(key)] 
	
	# to find the direction 
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)): 
		
		# check the direction of flow 
		# reverse the direction if we've just 
		# filled the top or bottom rail 
		if (row == 0) or (row == key - 1): 
			dir_down = not dir_down 
		
		# fill the corresponding alphabet 
		rail[row][col] = text[i] 
		col += 1
		
		# find the next row using 
		# direction flag 
		if dir_down: 
			row += 1
		else: 
			row -= 1
	# now we can construct the cipher 
	# using the rail matrix 
	result = [] 
	for i in range(key): 
		for j in range(len(text)): 
			if rail[i][j] != '\n': 
				result.append(rail[i][j]) 
	return("" . join(result)) 

'''text = input('Enter the string : ')
key = int(input('Enter the Key : '))
print(encryptRailFence(text , key))'''
