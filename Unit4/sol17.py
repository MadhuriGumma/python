# Problem17: Lycherel Numbers
def is_pal(z):
	s = str(z)
	for i in range(len(s)>>1):
		if s[i] != s[len(s) - 1 - i]:
			return False
	return True
def reverse(ss):
	s = str(ss)
	r = ""
	for i in range(len(s)):
		r = s[i] + r
	return r
def add(x):
	y = reverse(str(x))
	return int(x) + int(y)
def is_prob_lych(x):
	c = 0
	while c <= 60:
		if is_pal(x):	
			return False
		c = c + 1
		x = add(x)
	return True

a = int(raw_input('enter lower limit: '))
b = int(raw_input('enter upper limit: '))
n = 0
lych = 0
pal = 0
for i in range(a, b + 1):
	if is_prob_lych(i):
		print i, " is probably lycherel."
		lych = lych + 1
	elif is_pal(i):
		pal = pal + 1
	else:
		n = n + 1
print "Natural palindromes: ", pal
print "Non-Lycherel numbers yielding a palindrome: ", n
print "Lycherels: ", lych
