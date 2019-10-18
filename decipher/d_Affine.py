
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




def affine_decrypt(cipher):
	key = [17,20]
	return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) 
					% 26) + ord('A')) for c in cipher ]) 
