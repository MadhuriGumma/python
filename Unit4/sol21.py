# Problem21: CaesarCipher

def encode(s, n):
	res = ""
	for ch in s:
		if ord(ch) >= 97 and ord(ch) <= 122:
			res += chr(97 + (ord(ch) - 97 + n)%26)
		else:
			res += ch
	return res

ch = raw_input('Enter e to encode, d to decode or q to quit:').lower()
while ch != 'e' and ch != 'd' and ch != 'q':
	ch = raw_input('Invalid entry!\nEnter e to encode, d to decode or q to quit:').lower()
if ch == 'e':
	s = raw_input("Input string: ")
	n = 0
	while n < 1 or n > 25:
		n = int(raw_input("Enter the rotation integer[1 - 25]: "))
	print 'Encoded string: ', encode(s, n)
elif ch == 'd':
	s = raw_input("Input string: ")
	w = raw_input("Search term: ")
	ch = raw_input("Part 1 or 2? : ")
	while ch not in ['1', '2']:
		ch = raw_input("Invalid input.\nPart 1 or 2? : ")
	if ch == '1':
		n = int(raw_input("Rotation: "))
		w = encode(w, n)
		if w in s:
			print "Decoded string; ", encode(s, 26 - n)
		else:
			print "Not found!"
	else:
		found = False
		for i in range(26):
			if w in encode(s, i):
				found = True
				print "Rotation: ", 26 - i
				print "Decoded string: ", encode(s, i) 
				break
		if found == False:
			print "Word does not occur in any rotation."
else:
	exit('Exiting...')
	

