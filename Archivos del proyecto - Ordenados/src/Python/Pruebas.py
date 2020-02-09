import math

def hash(key):
	return sum([ord(c) for c in key])%31

print(hash('C_G'))