# Problem 26: CaesarCipher
freq = {}
t_f = [0]*26
text = ''

def readfreq(ff):
	global freq
	r = readfromfile(ff).split("\n")
	for l in r:
		a = l.split("\t")
		freq[a[0]] = float(a[1])

def countfreq(s):
	t_f = [0]*26
	for i in range(26):
		t_f[i] = s.count(chr(97+i))
	return t_f

def readfromfile(ff):
	r = ''
	with open(ff) as f:
		r = f.read().strip()
	return r

def shift(s, off):	
	r = ''
	for c in s:
		r = r + chr(97 + (ord(c)+off-97)%26)
	return r

def decrypt(text):
	m = max(t_f)
	print m
	i = 0
	r = ''
	while m in t_f[i:]:
		ind = t_f[i:].index(m)
		print ind
		r = shift(text, (ind - 5 + 26)%26)
		print r
		i = ind + 1
	return r

if __name__ == '__main__':
	readfreq('letter_frequencies.txt')
	countfreq('cipher1.txt')
	decrypt("ifmmpffff")
