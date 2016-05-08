def is_prime(num):
	'''Return True if a given non-negative integer is prime.'''
	# 0 and 1 are not prime numbers.
	if num==0 or num==1:
		return False
	
	# Loops over possible factors. If it doesn't find one, must be prime.
	for i in range(2, int(num**(1/2))+1):
		if num%i==0:
			return False
		
	return True

def brute_prime(seed):
	'''Takes a non-negative int and returns the next prime that is >= to it.'''
	while not is_prime(seed):
		seed += 1
	
	return seed

def euclid_gcd(m, n):
	'''Returns the greatest common divisor of two non-negative integers, using 
	Euclid's algorithm.'''
	while(n!=0):
		r = m%n
		m = n
		n = r
	
	return m

def extended_euclid(e, phi):
	'''Calculates the modular multiplicative inverse of e and phi, according to
	the extended Euclidean algorithm'''
	i = 0
	q_1 = 0
	q = 0
	carrys = {'tot': phi, 'quot': e, 'rem': (phi%e)}
	while (carrys['rem']!=0):
		q_2 = q_1
		q_1 = q
		q = carrys['tot'] // carrys['quot']
		if i==0:
			p = 0
		elif i==1:
			p_1 = p
			p = 1
		else:
			p_2 = p_1
			p_1 = p
			p = (p_2 - p_1*q_2) % phi
		carrys['tot'] = carrys['quot']
		carrys['quot'] = carrys['rem']
		carrys['rem'] = carrys['tot'] % carrys['quot']
		i += 1

	for k in range(0, 2):
		q_2 = q_1
		q_1 = q
		q = carrys['tot'] // carrys['quot']
		if i==0:
			p = 0
		elif i==1:
			p_1 = p
			p = 1
		else:
			p_2 = p_1
			p_1 = p
			p = (p_2 - p_1*q_2) % phi
		i += 1
	return p


def num2txt(num, k=3):
	'''Converts an integer that encodes a string back to the string. Each k 
	digits in the integer represents a unicode character. The leading zeros of 
	the first character are suppressed.'''
	txt = ""
	# Converts the integer to a string, for easy slicing. Will remove decrypted
	# digits as they are processed.
	num_str = str(num)
	
	# Decrypts the first character of the string, accounting for any leading
	# zeros, and removes the digits from the integer.
	txt += chr(int(num_str[0:len(num_str)%k]))
	num_str = num_str[len(num_str)%k:]
	
	# Loops over the remaining digits and decrypts them.
	for i in range(0, len(num_str)//k):
		txt += chr(int(num_str[0:k]))
		num_str = num_str[k:]
	
	return txt

def rsa(min_p, min_q, min_e):
	'''Generates a private key d and a public key (e, n) based on three inputs
	that are used to seed the key's variables.'''
	
	# Determines p and q such that they are the smallest primes greater than or
	# equal to min_p and min_q. These determine the value of n and phi.
	p = brute_prime(min_p)
	q = brute_prime(min_q)
	n = p*q
	phi = (p-1)*(q-1)
	
	# Determines e such that it is greater than or equal to min_e, and is
	# coprime to phi.
	e = min_e
	while(euclid_gcd(e, phi) != 1):
		e = brute_prime(e+1)
	
	# Sets d to the multiplicative inverse of e with respect to phi.
	d = extended_euclid(e, phi)

	print("The public key is :", e, n)
	
	return (d, e, n)

def rsa_decrypt(c, d, n, k=3):
	'''Uses a private key d to decrypt a numeric message contained in variable 
	c, using a k-digit size decryption.'''
	msg_num = (c**d) % n
	
	# Converts the integer representation back to a string.
	return num2txt(msg_num, k)