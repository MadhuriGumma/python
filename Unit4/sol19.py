# Problem 19: Hangman
from random import randint
freq = [["e"],["i","t"],["s","a","n"],["h","u","r","d","m"],["w","g","v","l","f","b","k"], ["o","p","j","x","c","z"], ["y","q"]]

def get_group(i):
	if i <= 70:
		return 0
	elif i <= 130:
		return 1
	elif i <= 180:
		return 2
	elif i <= 220:
		return 3
	elif i <= 250:
		return 4
	elif i <= 270:
		return 5
	elif i <= 280:
		return 6
	else:
		return -1

def get_rand_guess(m):
	cfreq = freq
	for i in range(len(cfreq)):
		for j in range(len(cfreq[i])):
			if cfreq[i][j] in m:
				cfreq[i].remove(cfreq[i][j])
				j = j-1	
	print cfreq
	r = get_group(randint(1,280))

	while len(cfreq[r]) == 0:
		r = get_group(randint(1,280))
	e = randint(0, len(cfreq[r]) - 1)
	return cfreq[r][e]

def is_char(c):
	i = ord(c)
	return (i >= 97 and i <= 122)

def add_char(ans, h, c):
	res = ""
	for i in range(len(ans)):
		if ans[i] == c:
			res = res+c
		else:
			res = res+h[i]
	return res

while True:
	ans = raw_input("Enter name to guess: ").lower()
	tries = int(raw_input("Enter max tries: "))
	for i in range(10):
		print "\n"
	missed = ""
	h = ""
	for i in ans:
		if is_char(i):
			h = h+"_"
		else:
			h = h+i
	while True:
		print "Guess:\n"+h+"\nExhausted: [ "+ missed +" ]\n"
		ch = raw_input("1. Guess yourself\n2. Ask computer to guess\n")
		if ch == "2":
			#comp guess
			g = get_rand_guess(missed)
			print "Guessed: ", g, "\n"
		else:
			gs = raw_input()
			g = str(gs[0]).lower()
		if g in ans:
			if g in h:
				print "Character used already.\n "+str(tries)+" tries remaining"
			else:
				h = add_char(ans, h, g)
				print "Correct!\n"+str(tries)+" tries remaining!\n\n"
				if "_" not in h:
					ch = raw_input("Game over. Continue?(y/n): ")
					if ch != "y" and ch != "Y":
						exit("Thank you for playing!")
					else:
						break
		else:
			tries = tries - 1
			missed = missed + g
			print "Incorrect! "+str(tries)+" tries left.\n"
			if tries == 0:
				print "Game over! Answer: "+ans+"\n\n"
				ch = raw_input("Continue?(y/n): ")
				if ch != "y" and ch != "Y":
					exit("Thank you for playing!")
				else:
					break

