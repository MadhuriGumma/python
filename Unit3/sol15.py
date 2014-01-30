# p15: Egyptian Multiplication
while True:
	print 'enter numbers to multiply:'
	x = a = int(raw_input('enter first number: '))
	y = b = int(raw_input('enter second number: '))
	prod = 0
	while b > 0:
		if b%2 == 1:
			prod += a
		b = int(b/2)
		a = a*2	
	print 'Product of ', x, ' and ', y, ' is: ', prod
	choice = raw_input('Do you want to continue?(y/n)')
	if choice != 'Y' and choice != 'y':
		exit('Quitting...')

