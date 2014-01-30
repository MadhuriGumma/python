# prob13: Persistence
def sum_digs(x):
	c = 0
	while x > 0:
		c += x%10
		x /= 10
	return c
def mult_digs(x):
	c = 1
	while x > 0:
		c *= x%10
		x /= 10
	return c
def add_pers(x):
	p = 0
	while x > 9:
		x = sum_digs(x)
		p += 1
	print 'add_pers: ', p
	print 'add_root: ', x
def mul_pers(x):
	p = 0
	while x > 9:
		x = mult_digs(x)
		p = p+1
	print 'mul_persistence: ', p
	print 'mul_root: ', x
n = int(raw_input('enter a number: '))
if n < 0:
	exit('invalid input')
add_pers(n)
mul_pers(n)
