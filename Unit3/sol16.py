# p16: Calculator
while True:
	s = raw_input('enter expression to evaluate: ')
	arr = s.split(" ")
	a = float(arr[0])
	b = float(arr[2])
	c = arr[1]
	if c == "+":
		res = a + b
		print 'Result: ', res
	elif c == "-":
		res = a - b
		print 'Result: ', res
	elif c == "*":
		res = a * b
		print 'Result: ', res
	elif c == "/":
		if b == 0:
			print 'Division by zero error!'
		else:
			res = a / b
			print 'Result: ', res
	else:
		print 'Invalid operator: ', c
	ch = raw_input('Continue?(y/n)')
	if ch != "Y" and ch != "y":
		print "Quitting..."
		break

