# Prob20: Mastermind
s = raw_input('Enter 4-digit key: ')
iarr = list("0123456789")
arr = list("0123456789")
for i in range(10):
	iarr[i] = 0
for i in s:
	if ord(i) >= 48 and ord(i) <= 57:
		iarr[ord(i) - 48] += 1
tries = 0
gs = []
while True:
	invalid = True
	while invalid:
		print 'Used guesses: ', gs
		invalid = False
		g = raw_input('Enter guess: ')
		#Rule 1
		if len(g) != 4:
			invalid = True
		if invalid:
			print 'Bad guess.'
			continue
		#Rule 2
		for i in range(10):
			arr[i] = 0
		for i in g:
			if ord(i) >= 48 and ord(i) <= 57:
				arr[ord(i) - 48] += 1
			else:
				invalid = True
				break
		if invalid:
			print 'Bad guess.'
			continue
		#Rule 3
		for i in range(10):
			if arr[i] > 1:
				invalid = True
				break
		if invalid:
			print 'Bad guess.'

	gs.append(g)
	tries += 1
	if g == s:
		print 'Correct! Used ', tries, 'tries.'
		break
	else:
		print 'Incorrect guess.'
		if tries == 12:
			print 'All tries used. Game over. Key: ', s
		else:
			c = 0
			d = 0
			for i in range(4):
				if s[i] == g[i]:
					d += 1
			print 'Correct digits: ', d
			for i in range(10):
				if arr[i] == 1 and iarr[i] == 1:
					c += 1
			print 'Wrong positions: ', c - d
