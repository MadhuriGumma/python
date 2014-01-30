# prob11: DigitCount
def count_digs(n, x):
	if x == 0:
		c = 1
	else:
		c = 0
	while n > 0:
		if n%10 == x:
			c += 1
		n /= 10
	return c
print count_digs(int(raw_input('enter number: ')), int(raw_input('enter digit: ')))
