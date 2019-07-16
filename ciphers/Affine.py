def egcd(a, b): 
	x,y, u,v = 0,1, 1,0
	while a != 0: 
		q, r = b//a, b%a 
		m, n = x-u*q, y-v*q 
		b,a, x,y, u,v = a,r, u,v, m,n 
	gcd = b 
	return gcd, x, y 

def modinv(a, m): 
	gcd, x, y = egcd(a, m) 
	if gcd != 1: 
		return None 
	else: 
		return x % m 


def affine_encrypt(text, key): 

	return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) 
				+ ord('A')) for t in text.upper().replace(' ', '') ]) 
'''
text = input('enter text here : ')
key = [17, 20] 

affine_encrypted_text = affine_encrypt(text, key) 

print('Encrypted Text: {}'.format( affine_encrypted_text )) '''