import math

def forwardNTT(a, q):
	n = len(a) + 1
	m = 2
	while (m <= n / 2):
		primitiveRoot = getPrimitiveRoot(m)
		omega = sqrtMod(primitiveRoot, q)
		j = 0
		while (j < n / 2):
			k = 0
			while (K < n):
				t = mod(omega * a[m / 2 + j + k], q)
				u = a[j + k]
				a[j + k] = mod(u + t, q)
				a[m / 2 + j + k] = mod(u - t, q)
				k += m
			omega *= primitiveRoot
			j += 1
		m *= 2

def mod(x, m):
	return (a % m + m) % m

def getPrimitiveRoot(m):
	# No idea how to get it
	return 0

def sqrtMod(pr, q):
	# Not implemented yet
	return 0