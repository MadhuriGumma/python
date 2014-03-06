# Problem 26: CaesarCipher
freq = {}
t_f = [0]*26
text = ''

def readfreq(ff):
	# reads letter freqs from file
	global freq
	r = readfromfile(ff).split("\n")
	for l in r:
		a = l.split("\t")
		freq[a[0]] = float(a[1])

def countfreq(s):
	# counts frequencies of letters in s
	t_f = [0]*26
	for i in range(26):
		t_f[i] = s.count(chr(97+i))
	return t_f

def readfromfile(ff):
	# reads a file
	r = ''
	with open(ff) as f:
		r = f.read().strip()
	return r

def shift(s, off):
	r = ''
	for c in s:
		if ord(c) > 96 and ord(c) < 123:
			r = r + chr(97 + (ord(c)+off-97)%26)
		else:
			r = r + c
	return r

def decrypt(text):
	lf = countfreq(text)
	max1 = max(lf)
	arr = [x for x in range(26) if lf[x] == max1]
	for a in arr:
		lf[a] = 0
		max2 = max(lf)
		brr = [x for x in range(26) if lf[x] == max2 and (a - 4)%26 == (x-19)%26]
		for b in brr:
			lf[b] = 0
			max3 = max(lf)
			crr = [x for x in range(26) if lf[x] == max3 and (a - 4)%26 == x]
			for c in crr:
				print shift(text, (4 - a)%26)
			lf[b] = max2
		lf[a] = max1


if __name__ == '__main__':
	readfreq('letter_frequencies.txt')
	countfreq('cipher1.txt')
	decrypt(readfromfile(raw_input()))
