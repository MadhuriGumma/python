# Problem 25: Scrambled words
from random import shuffle
def process(fn):
	with open(fn) as f:
		words = f.read().split(" ")
		res = ''
	for w in words:
		w = w.strip()
		l = ord(w[-1])
		if (l >= 65 and l <= 90) or (l >= 97 and l <= 122):
			l = 0
		else:
			w = w[:-1]
		if len(w) > 3:
			n = list(w[1:-1])
			shuffle(n)
			n = ''.join(n)
			n = w[0] + n + w[-1]
		else:
			n = w
		n = n+chr(l)
		res = res+' '+n
	return res
if __name__ == '__main__':
	print process(raw_input('Enter filename: '))
