# def rearrange(a):
# 	n = len(a)
# 	i = 0
# 	while (i < n // 2):
# 		bit1 = i % 2
# 		bit2 = (i >> 1) % 2
# 		bit3 = (i >> 2) % 2
# 		bit4 = (i >> 3) % 2
# 		bit5 = (i >> 4) % 2
# 		bit6 = (i >> 5) % 2
# 		bit7 = (i >> 6) % 2
# 		bit8 = (i >> 7) % 2
# 		swpIdx = bit1 * 128 + bit2 * 64 + bit3 * 32 + bit4 * 16 + bit5 * 8 + bit6 * 4 + bit7 * 2 + bit8
# 		if (swpIdx > i):
# 			i2 = i << 1
# 			swp2 = swpIdx << 1
# 			a[i2] ^= a[swp2]
# 			a[swp2] ^= a[i2]
# 			a[i2] ^= a[swp2]
# 			a[i2 + 1] ^= a[swp2 + 1]
# 			a[swp2 + 1] ^= a[i2 + 1]
# 			a[i2 + 1] ^= a[swp2 + 1]
# 		i += 1
# 	return a

# def forwardNTT(a, mod):
# 	n = len(a)
# 	#bit reversing
# 	i = 1
# 	j = 0
# 	while (i < n):
# 		bit = n >> 1;
# 		while (j >= bit):
# 			j -= bit
# 			bit >>= 1
# 		j += bit
# 		if (i < j):
# 			a[i] ^= a[j]
# 			a[j] ^= a[i]
# 			a[i] ^= a[j]
# 		i += 1
# 	#end of bit reversing
# 	m = 2
# 	i = 0
# 	while (m <= n // 2):
# 		primitiveRoot = primrtOmegaTable[i] #primitiveRoot = getPrimitiveRoot(m)
# 		omega = primrtOmegaTable[i + 1] #omega = sqrtMod(primitiveRoot, q)
# 		j = 0
# 		while (j < m // 2):
# 			k = 0
# 			while (k < n):
# 				t = modulus(omega * a[m // 2 + j + k], mod)
# 				u = a[j + k]
# 				a[j + k] = modulus(u + t, mod)
# 				a[m // 2 + j + k] = modulus(u - t, mod)
# 				k += m
# 			omega *= primitiveRoot
# 			omega = modulus(omega, q)
# 			j += 1
# 		m *= 2
# 		i += 1
# 	return a

# def forwardNTT2(a, mod):
# 	n = len(a)
# 	#bit reversing
# 	# i = 1
# 	# j = 0
# 	# while (i < n):
# 	# 	bit = n >> 1;
# 	# 	while (j >= bit):
# 	# 		j -= bit
# 	# 		bit >>= 1
# 	# 	j += bit
# 	# 	if (i < j):
# 	# 		a[i] ^= a[j]
# 	# 		a[j] ^= a[i]
# 	# 		a[i] ^= a[j]
# 	# 	i += 1
# 	#end of bit reversing
# 	i = 0
# 	m = 2
# 	while (m <= n // 2):
# 		primitiveRoot = primrtOmegaTable[i]
# 		omega = primrtOmegaTable[i + 1]
# 		i += 1
# 		j = 0
# 		while (j < m):
# 			k = 0
# 			while (k < n): # it is n // 2 in the paper
# 				# if (j + k + m < n): # this is added by me
# 				u1 = a[j + k]
# 				t1 = modulus(omega * a[j + k + 1], mod)
# 				u2 = a[j + k + m]
# 				t2 = modulus(omega * a[j + k + m + 1], mod)
# 				a[j + k] = modulus(u1 + t1, mod)
# 				a[j + k + 1] = modulus(u2 + t2, mod)
# 				a[j + k + m] = modulus(u1 - t1, mod)
# 				a[j + k + m + 1] = modulus(u2 - t2, mod)
# 				k = k + 2 * m
# 			omega *= primitiveRoot
# 			omega = modulus(omega, mod)
# 			j += 2
# 		m *= 2
# 	primitiveRoot = FWD_CONST1
# 	omega = FWD_CONST2
# 	j = 0
# 	while (j < n // 2):
# 		t1 = omega * a[2 * j + 1]
# 		t1 = modulus(t1, mod)
# 		u1 = a[2 * j]
# 		a[2 * j] = modulus(u1 + t1, mod)
# 		a[2 * j + 1] = modulus(u1 - t1, mod)
# 		omega = omega * primitiveRoot
# 		omega = modulus(omega, mod)
# 		j += 1
# 	return a

# def InvNTT2(a, mod):
# 	n = len(a)
# 	#bit reversing
# 	# i = 1
# 	# j = 0
# 	# while (i < n):
# 	# 	bit = n >> 1;
# 	# 	while (j >= bit):
# 	# 		j -= bit
# 	# 		bit >>= 1
# 	# 	j += bit
# 	# 	if (i < j):
# 	# 		a[i] ^= a[j]
# 	# 		a[j] ^= a[i]
# 	# 		a[i] ^= a[j]
# 	# 	i += 1
# 	#end of bit reversing
# 	primitiveRoot = 0
# 	m = 2
# 	while (m <= n // 2):
# 		if (m == 2):
# 			primitiveRoot = 12288
# 		elif (m == 4):
# 			primitiveRoot = 10810
# 		elif (m == 8):
# 			primitiveRoot = 7143
# 		elif (m == 16):
# 			primitiveRoot = 10984
# 		elif (m == 32):
# 			primitiveRoot = 3542
# 		elif (m == 64):
# 			primitiveRoot = 4821
# 		elif (m == 128):
# 			primitiveRoot = 1170
# 		elif (m == 256):
# 			primitiveRoot = 5755
# 		omega = 1
# 		j = 0
# 		while (j < m // 2):
# 			k = 0
# 			while (k < n // 2):
# 				t1 = omega * a[2 * (k + j) + 1]
# 				t1 = modulus(t1, mod)
# 				u1 = a[2 * (k + j)]
# 				t2 = omega * a[2 * (k + j + m // 2) + 1]
# 				t2 = modulus(t2, mod)
# 				u2 = a[2 * (k + j + m // 2)]
# 				a[2 * (k + j)] = modulus(u1 + t1, mod)
# 				a[2 * (k + j + m // 2)] = modulus(u1 - t1, mod)
# 				a[2 * (k + j) + 1] = modulus(u2 + t2, mod)
# 				a[2 * (k + j + m // 2) + 1] = modulus(u2 - t2, mod)
# 				k += m
# 			omega = omega * primitiveRoot;
# 			omega = modulus(omega, mod);
# 			j += 1
# 		m *= 2
# 	primitiveRoot = INVCONST1
# 	omega = 1
# 	j = 0
# 	while (j < n):
# 		u1 = a[j]
# 		j += 1
# 		t1 = omega * a[j]
# 		t1 = modulus(t1, mod)
# 		a[j - 1] = modulus(u1 + t1, mod)
# 		a[j] = modulus(u1 - t1, mod)
# 		j += 1
# 		omega = omega * primitiveRoot
# 		omega = modulus(omega, mod)
# 	omega2 = INVCONST2
# 	primitiveRoot = INVCONST3
# 	omega = 1
# 	j = 0
# 	while (j < n):
# 		a[j] = modulus(omega * a[j], mod)
# 		a[j] = modulus(a[j] * SCALING, mod)
# 		j += 1
# 		a[j] = modulus(omega2 * a[j], mod)
# 		a[j] = modulus(a[j] * SCALING, mod)
# 		j += 1
# 		omega = omega * primitiveRoot
# 		omega = modulus(omega, mod)
# 		omega2 = omega2 * primitiveRoot
# 		omega2 = modulus(omega2, mod)
# 	return a

# p1 = [5, 2, 4, 3] + ([0] * (M - 4))
# p2 = [3, 1, 2, 1] + ([0] * (M - 4))
# print("p1 = ")
# print(p1)
# print("p2 = ")
# print(p2)
# # lol = coefficientSub(p1, p2, q)
# # print("p1 - p2 = ")
# # print(lol)
# forwardNTT2(p1, q)
# rearrange(p1)
# forwardNTT2(p2, q)
# rearrange(p2)
# lol2 = coefficientMul(p1, p2, q)
# print("NTT(p1 * p2) = ")
# print(lol2)
# InvNTT2(lol2, q)
# rearrange(lol2)
# print("INVNTT(NTT(p1 * p2)) = ")
# print(lol2)

# p3 = coefficientAdd(p1, p2, q)
# print(p3)
# forwardNTT2(p1, q)
# forwardNTT2(p2, q)
# p6 = coefficientAdd(p1, p2, q)
# print(p6)
# InvNTT2(p6, q)
# print(p6)