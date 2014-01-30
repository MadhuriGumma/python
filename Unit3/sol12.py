# prob12: LatinSquares
n = int(raw_input('enter order: '))
a = int(raw_input('enter top-left: '))
if a < 1 or a > n:
	exit("invalid offset")
for i in range(n):
	s = ""
	for j in range(n):
		s = s + " " + str(1 + (a + i + j - 1)%n)
	print s
print "=================================="
