q = 12289
M = 512
primitiveRoot = 3
sqrtOfPrimitiveRoot = 1321
primitiveRootInverse = 8193

def modPow(n, p, mod):
	if (p == 0):
		return 1
	if (p == 1):
		return n % mod
	if ((p & 1) == 0):
		x = modPow(n, p >> 1, mod)
		x *= x
		return x % mod
	return (n * modPow(n, p - 1, mod)) % mod

def primitiveRootCheck(r, n, mod):
	x = modPow(r, n, mod)
	if (x != 1):
		return False
	i = 1
	while (i < n):
		x = modPow(r, i, mod)
		if (x == 1):
			return False
		i += 1
	return True;

def findPrimitiveRoots(n, mod):
	i = 0
	while (i < mod):
		if (primitiveRootCheck(i, M, mod)):
			print(i)
		i += 1
	return

#findPrimitiveRoots(M, q)

def NTT(a, w, mod):
	n = len(a)
	#bit reversing
	i = 1
	j = 0
	while (i < n):
		bit = n >> 1;
		while (j >= bit):
			j -= bit
			bit >>= 1
		j += bit
		if (i < j):
			a[i] ^= a[j]
			a[j] ^= a[i]
			a[i] ^= a[j]
		i += 1
	#end of bit reversing
	m = 2
	while (m <= n):
		s = 0
		while (s < n):
			i = 0
			while (i < m // 2):
				N = i * n // m
				aa = s + i
				b = s + i + m // 2
				c = a[aa]
				d = a[b]
				a[aa] = (c + modPow(w, int(N % n), mod) * d) % mod
				a[b] = (c - modPow(w, int(N % n), mod) * d) % mod
				i += 1
			s += m
		m <<= 1
	return a

# p = [1, 2, 3, 4, 5, 6] + ([0] * (M - 6))
# NTT(p, primitiveRoot, q)
# print(p)


print((sqrtOfPrimitiveRoot * sqrtOfPrimitiveRoot) % q)
print(q % (M << 1))