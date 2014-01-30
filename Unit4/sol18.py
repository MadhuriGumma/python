# Problem18: NumberGuessing
acc = False
while True:
	try:
		s = raw_input('enter a 5-digit number with no repeated digits: ')
		num = s
		n = int(s)
		d = dict()
		acc = True
		for i in s:
			if i in d:
				d[i] += 1
				acc = False
			else:
				d[i] = 1
		num_dict = d
		if acc:
			if len(s) != 5:
				print 'Only 5 digit numbers, please'
			else:
				break
	except ValueError:
		exit('A number! How hard can it be?')
for i in range(20):
	print "\n"
max = 10
tries = 0
while True:
	tries += 1
	acc = False
	while True:
		s = raw_input('guess the number: ')
		try:
			n = int(s)
			if len(s) == 5:
				acc = True
			if acc:	
				break
			else:
				print "Invalid input!"
		except ValueError:
			print "Invalid input!"
			continue
	d = dict()
	corr = 0
	corr_pos = 0
	for i in range(len(s)):
		if s[i] not in d:
			d[s[i]] = 1;
			if s[i] in num_dict:
				corr += 1
			if s[i] == num[i]:
				corr_pos += 1
	print 'Correct digits: ', corr
	print 'Correct position: ', corr_pos
	print 'Tries: ', tries
	if tries == 10:
		exit("Could not guess! Number was "+ str(num))
	if corr == 5 and corr_pos == 5:
		exit("Correct guess in "+ str(tries) + " tries!")

