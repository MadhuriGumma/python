# Problem 22: ROck, Paper, Scissors
from random import randint
valid = ['r', 'p', 's', 'q']
def input():
	return raw_input('Enter R/r for rock, P/p for paper, S/s for scissors, Q/q to quit: ').lower()
usr = 0
comp = 0
r = 0
p = 0
s = 0
t = 0
def choose():
	anti = {'r': 'p', 'p': 's', 's': 'r'}
	m = max(r, p, s)
	arr = []
	if r == m:
		arr.append('r')
	if p == m:
		arr.append('p')
	if s == m:
		arr.append('s')
	return anti[arr[randint(0, len(arr) - 1)]]
while True:
	ch = choose()
	inp = input()
	while inp not in valid:
		print "Invalid input!"
		inp = input()
	if inp == 'q':
		print "Choices: R ", r, "\tP ", p, "\tS ", s
	else:
		if ch == inp:
			t += 1
			if inp == 'r':
				r += 1
			if inp == 'p':
				p += 1
			if inp == 's':
				s += 1
			
			print "Tie!"
		elif inp == 'r' and ch == 'p':
			r += 1
			print "Paper wraps rock!"
			comp += 1
		elif inp == 'p' and ch == 's':
			p += 1
			print "Scissors cut paper"
			comp += 1
		elif inp == 's' and ch == 'r':
			s += 1
			print "Rock beats scissors"
			comp += 1
		elif inp == 'r' and ch == 's':
			r += 1
			print "Rock beats scissors"
			usr += 1
		elif inp == 'p' and ch == 'r':
			p += 1
			print "Paper wraps rock!"
			usr += 1
		elif inp == 's' and ch == 'p':
			s += 1
			print "Scissors cut paper"
			usr += 1
		print "Scores: User " + str(usr) + "\tComp " + str(comp) + "\tTie "+str(t)
		print "Choices: R ", r, "\tP ", p, "\tS ", s
