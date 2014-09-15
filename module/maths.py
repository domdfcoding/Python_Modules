def gcd(a, b):
	# Returns the GCD (HCF) of a and b using Euclid's Algorithm
	while a != 0:
		a, b = b % a, a
	return b
	
def gcd2(numbers):
	# Returns the GCD (HCF) of a list of numbers using Euclid's Algorithm
	c = numbers[0]
	for i in range(1, (len(numbers))):
		c = gcd(c,numbers[i])
	return c
	
def lcm(numbers):
	# Returns the LCM of a list of numbers using Euclid's Algorithm
	product = numbers[0]
	for i in range(1, len(numbers)):
		product = product * numbers[i]
	gcd=gcd2(numbers)
	lcm = product/gcd
	if product%gcd == 0:
		return lcm
	else: return product
	
def hcf(a,b):
	gcd(a,b)

def hcf2(numbers):
	gcd2(numbers)
	
def modInverse(a,m):  # Returns the modular inverse of a % m,
	# which is the number x such that a*x % m = 1
	if gcd(a,m) != 1:
		return None # No mod inverse exists if a & m aren't relatively prime
	
	
	# Calculation using the Extended Euclidean Algorithm
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, m
	while v3 != 0:
		q = u3 // v3 # // forces integer division in Python 3
		v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
	return u1 % m

def isint(num):	# Only works with floating point numbers
	if num == int(num):
		return True
	else:
		return False
